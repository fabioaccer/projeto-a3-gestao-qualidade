import SQLite from 'sqlite3';

export class DatabaseManager {
    
    static _instance = null;

    constructor() {
        if (DatabaseManager._instance) {
            throw new Error('Use DatabaseManager.getInstance() instead of new operator');
        }

        this._db = new SQLite.Database('./budget.db', (err) => {
            if (err) {
                console.error('Database connection error:', err.message);
            } else {
                console.log('Connected to the SQLite database.');
                this._initializeDatabase();
            }
        });

        DatabaseManager._instance = this;
    }

    static getInstance() {
        if (!DatabaseManager._instance) {
            DatabaseManager._instance = new DatabaseManager();
        }
        return DatabaseManager._instance;
    }

    getConnection() {
        return this._db;
    }

    _initializeDatabase() {
        const createTransactionsTable = `
      CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        type TEXT NOT NULL,
        date TEXT NOT NULL
      )
    `;

        this._db.run(createTransactionsTable);
    }

    closeConnection() {
        return new Promise((resolve, reject) => {
            this._db.close((err) => {
                if (err) {
                    reject(err);
                } else {
                    DatabaseManager._instance = null;
                    resolve();
                }
            });
        });
    }

}