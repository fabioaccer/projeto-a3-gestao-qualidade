export class Transaction {

    constructor(id, title, amount, category, paymentMethod, type, date) {
        this._id = id;
        this._title = title;
        this._amount = amount;
        this._category = category;
        this._paymentMethod = paymentMethod;
        this._type = type; // 'income' ou 'expense'
        this._date = date;
    }

    get id() { return this._id; }

    get title() { return this._title; }
    set title(value) { this._title = value; }

    get amount() { return this._amount; }
    set amount(value) {
        if (isNaN(value) || value <= 0) {
            throw new Error('O valor deve ser um número positivo');
        }
        this._amount = value;
    }

    get category() { return this._category; }
    set category(value) { this._category = value; }

    get paymentMethod() { return this._paymentMethod; }
    set paymentMethod(value) { this._paymentMethod = value; }

    get type() { return this._type; }
    set type(value) {
        if (value !== 'income' && value !== 'expense') {
            throw new Error('O tipo deve ser "income" ou "expense"');
        }
        this._type = value;
    }

    get date() { return this._date; }
    set date(value) { this._date = value; }

    isExpense() {
        return this._type === 'expense';
    }

    isIncome() {
        return this._type === 'income';
    }

    toStorageFormat() {
        return {
            id: this._id,
            title: this._title,
            amount: this._amount,
            category: this._category,
            payment_method: this._paymentMethod,
            type: this._type,
            date: this._date
        };
    }

    static fromStorageFormat(data) {
        return new Transaction(
            data.id,
            data.title,
            data.amount,
            data.category,
            data.payment_method || data.paymentMethod,
            data.type,
            data.date
        );
    }

    validate() {
        if (!this._title || this._title.trim() === '') {
            throw new Error('O título é obrigatório');
        }

        if (isNaN(this._amount) || this._amount <= 0) {
            throw new Error('O valor deve ser um número positivo');
        }

        if (!this._category || this._category.trim() === '') {
            throw new Error('A categoria é obrigatória');
        }

        if (!this._paymentMethod || this._paymentMethod.trim() === '') {
            throw new Error('O método de pagamento é obrigatório');
        }

        if (this._type !== 'income' && this._type !== 'expense') {
            throw new Error('O tipo deve ser "income" ou "expense"');
        }

        if (!this._date) {
            throw new Error('A data é obrigatória');
        }

        return true;
    }
}