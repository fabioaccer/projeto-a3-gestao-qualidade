import { Transaction } from '../../server/models/Transaction';

export class Income extends Transaction {
    constructor(id, title, amount, category, paymentMethod, date) {
        super(id, title, amount, category, paymentMethod, 'income', date);
    }

    getFormattedAmount() {
        return `+$${this._amount.toFixed(2)}`;
    }
}