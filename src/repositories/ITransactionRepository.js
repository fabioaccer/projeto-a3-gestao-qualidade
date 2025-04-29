export class ITransactionRepository {
    async add(transaction) { throw new Error('Método não implementado'); }
    async getById(id) { throw new Error('Método não implementado'); }
    async getAll() { throw new Error('Método não implementado'); }
    async update(transaction) { throw new Error('Método não implementado'); }
    async delete(id) { throw new Error('Método não implementado'); }
    async getWeeklyExpenses() { throw new Error('Método não implementado'); }
    async getMonthlyExpenses() { throw new Error('Método não implementado'); }
    async getTransactionsByCategory() { throw new Error('Método não implementado'); }
    async getAmountByPaymentMethod() { throw new Error('Método não implementado'); }
    async getTopCategories(limit) { throw new Error('Método não implementado'); }
}