import os
import csv
import datetime
import sqlite3

DB_FILE = 'expenses.db'

class ExpenseTracker:
    def __init__(self, db_file=DB_FILE):
        self.conn = sqlite3.connect(db_file)
        self._create_tables()

    def _create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS budget (
                    month TEXT PRIMARY KEY,
                    amount REAL NOT NULL
                )
            ''')

    def add_expense(self, amount, category, description="", date=None):
        if not date:
            date = datetime.date.today().isoformat()
        with self.conn:
            self.conn.execute(
                'INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)',
                (amount, category, description, date)
            )

    def get_total_spent(self, month):
        cur = self.conn.cursor()
        cur.execute(
            'SELECT SUM(amount) FROM expenses WHERE strftime("%Y-%m", date) = ?',
            (month,)
        )
        result = cur.fetchone()[0]
        return result if result else 0.0

    def get_summary_by_category(self, month):
        cur = self.conn.cursor()
        cur.execute(
            'SELECT category, SUM(amount) FROM expenses WHERE strftime("%Y-%m", date) = ? GROUP BY category',
            (month,)
        )
        return dict(cur.fetchall())

    def set_monthly_budget(self, month, amount):
        with self.conn:
            self.conn.execute('REPLACE INTO budget (month, amount) VALUES (?, ?)', (month, amount))

    def is_budget_exceeded(self, month):
        budget = self.get_budget(month)
        spent = self.get_total_spent(month)
        return spent > budget if budget else False

    def get_budget(self, month):
        cur = self.conn.cursor()
        cur.execute('SELECT amount FROM budget WHERE month = ?', (month,))
        row = cur.fetchone()
        return row[0] if row else None

    def export_to_csv(self, filename, month):
        cur = self.conn.cursor()
        cur.execute(
            'SELECT amount, category, description, date FROM expenses WHERE strftime("%Y-%m", date) = ?',
            (month,)
        )
        rows = cur.fetchall()
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Amount', 'Category', 'Description', 'Date'])
            writer.writerows(rows)

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(50.0, 'Groceries', 'Bought fruits and veggies')
    tracker.set_monthly_budget('2025-05', 500.0)
    print("Total spent:", tracker.get_total_spent('2025-05'))
    print("Summary by category:", tracker.get_summary_by_category('2025-05'))
    print("Budget exceeded:", tracker.is_budget_exceeded('2025-05'))
    tracker.export_to_csv('may_expenses.csv', '2025-05')
    tracker.close()