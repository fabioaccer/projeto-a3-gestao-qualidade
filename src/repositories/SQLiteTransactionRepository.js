import { ITransactionRepository } from './ITransactionRepository';
import { Transaction, Expense, Income } from '../models';
import { DatabaseManager } from '../services/database/DatabaseManager';

export class SQLiteTransactionRepository extends ITransactionRepository {
    constructor() {
        super();
        this.db = DatabaseManager.getInstance().getConnection();
    }

    async add(transaction) {
        transaction.validate();

        return new Promise((resolve, reject) => {
            const storageFormat = transaction.toStorageFormat();

            const sql = `
        INSERT INTO transactions (title, amount, category, payment_method, type, date)
        VALUES (?, ?, ?, ?, ?, ?)
      `;

            this.db.run(
                sql,
                [
                    storageFormat.title,
                    storageFormat.amount,
                    storageFormat.category,
                    storageFormat.payment_method,
                    storageFormat.type,
                    storageFormat.date
                ],
                function (err) {
                    if (err) {
                        reject(err);
                    } else {
                        transaction._id = this.lastID;
                        resolve(transaction);
                    }
                }
            );
        });
    }

    async getById(id) {
        return new Promise((resolve, reject) => {
            const sql = `SELECT * FROM transactions WHERE id = ?`;

            this.db.get(sql, [id], (err, row) => {
                if (err) {
                    reject(err);
                } else if (!row) {
                    resolve(null);
                } else {
                    const transaction = this._createTransactionFromRow(row);
                    resolve(transaction);
                }
            });
        });
    }

    async getAll() {
        return new Promise((resolve, reject) => {
            const sql = `SELECT * FROM transactions ORDER BY date DESC`;

            this.db.all(sql, [], (err, rows) => {
                if (err) {
                    reject(err);
                } else {
                    const transactions = rows.map(row => this._createTransactionFromRow(row));
                    resolve(transactions);
                }
            });
        });
    }

    async update(transaction) {
        transaction.validate();

        return new Promise((resolve, reject) => {
            const storageFormat = transaction.toStorageFormat();

            const sql = `
        UPDATE transactions 
        SET title = ?, amount = ?, category = ?, payment_method = ?, type = ?, date = ?
        WHERE id = ?
      `;

            this.db.run(
                sql,
                [
                    storageFormat.title,
                    storageFormat.amount,
                    storageFormat.category,
                    storageFormat.payment_method,
                    storageFormat.type,
                    storageFormat.date,
                    storageFormat.id
                ],
                function (err) {
                    if (err) {
                        reject(err);
                    } else {
                        resolve(transaction);
                    }
                }
            );
        });
    }

    async delete(id) {
        return new Promise((resolve, reject) => {
            const sql = `DELETE FROM transactions WHERE id = ?`;

            this.db.run(sql, [id], function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve(this.changes > 0);
                }
            });
        });
    }

    async getWeeklyExpenses() {
        return new Promise((resolve, reject) => {
            const oneWeekAgo = new Date();
            oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
            const oneWeekAgoStr = oneWeekAgo.toISOString().split('T')[0];

            const sql = `
        SELECT SUM(amount) as totalExpense
        FROM transactions
        WHERE type = 'expense' AND date >= ?
      `;

            this.db.get(sql, [oneWeekAgoStr], (err, row) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(row.totalExpense || 0);
                }
            });
        });
    }

    async getMonthlyExpenses() {
        return new Promise((resolve, reject) => {
            const oneMonthAgo = new Date();
            oneMonthAgo.setMonth(oneMonthAgo.getMonth() - 1);
            const oneMonthAgoStr = oneMonthAgo.toISOString().split('T')[0];

            const sql = `
        SELECT SUM(amount) as totalExpense
        FROM transactions
        WHERE type = 'expense' AND date >= ?
      `;

            this.db.get(sql, [oneMonthAgoStr], (err, row) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(row.totalExpense || 0);
                }
            });
        });
    }

    async getTransactionsByCategory() {
        return new Promise((resolve, reject) => {
            const sql = `
        SELECT category, COUNT(*) as count
        FROM transactions
        GROUP BY category
        ORDER BY count DESC
      `;

            this.db.all(sql, [], (err, rows) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(rows);
                }
            });
        });
    }

    async getAmountByPaymentMethod() {
        return new Promise((resolve, reject) => {
            const sql = `
        SELECT payment_method, type, SUM(amount) as totalAmount
        FROM transactions
        GROUP BY payment_method, type
      `;

            this.db.all(sql, [], (err, rows) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(rows);
                }
            });
        });
    }

    async getTopCategories(limit = 5) {
        return new Promise((resolve, reject) => {
            const sql = `
        SELECT category, SUM(amount) as totalAmount
        FROM transactions
        WHERE type = 'expense'
        GROUP BY category
        ORDER BY totalAmount DESC
        LIMIT ?
      `;

            this.db.all(sql, [limit], (err, rows) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(rows);
                }
            });
        });
    }

    _createTransactionFromRow(row) {
        if (row.type === 'expense') {
            return new Expense(
                row.id,
                row.title,
                row.amount,
                row.category,
                row.payment_method,
                row.date
            );
        } else {
            return new Income(
                row.id,
                row.title,
                row.amount,
                row.category,
                row.payment_method,
                row.date
            );
        }
    }
}