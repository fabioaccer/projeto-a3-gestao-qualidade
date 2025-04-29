import { Transaction } from '../../server/models/Transaction';

export class Expense extends Transaction {
    constructor(id, title, amount, category, paymentMethod, date) {
        super(id, title, amount, category, paymentMethod, 'expense', date);
    }

    getFormattedAmount() {
        return `-$${this._amount.toFixed(2)}`;
    }
}