from stack import Stack
from queue import Queue

class Calculator:
    def __init__(self):
        self.precedence = {
            '(': 0, ')': 0,
            '**': 4, '^': 4,
            '*': 2, '/': 2,
            '+': 1, '-': 1,
        }
        self.operators = ['**', '*', '/', '+', '-', '^', '(', ')']
        self.previous_results = []

    def infix_to_postfix_and_evaluate(self, expression):
        stack = Stack()
        postfix = Queue()

        # Преобразование инфиксного выражения в постфиксное
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            
            if expression[i] == '(':
                stack.push(expression[i])

            elif expression[i] == ')':
                while stack.peek() != '(':
                    postfix.put(stack.pop())
                stack.pop()  # Удалить '(' из стека

            elif expression[i] in self.operators:
                op = expression[i]
                if expression[i] == '^':
                    op = '^'  # Здесь используем '^' вместо '**'
                elif expression[i] == '*' and i+1 < len(expression) and expression[i+1] == '*':
                    op = '**'
                    i += 1
                while not stack.is_empty() and self.precedence[stack.peek()] >= self.precedence[op]:
                    postfix.put(stack.pop())
                stack.push(op)

            else:
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                postfix.put(num)
                i -= 1

            i += 1

        while not stack.is_empty():
            postfix.put(stack.pop())

        # Собираем постфиксное выражение
        postfix_expression = []
        while not postfix.empty():
            postfix_expression.append(postfix.get())

        # Выводим постфиксную запись
        postfix_str = ' '.join(postfix_expression)
        print("Постфиксная запись:", postfix_str)

        # Функция для вычисления значения постфиксного выражения
        def evaluate_postfix(postfix_expression):
            eval_stack = Stack()

            for token in postfix_expression:
                if token.replace('.', '', 1).isdigit():
                    eval_stack.push(float(token) if '.' in token else int(token))
                else:
                    operand2 = eval_stack.pop()
                    operand1 = eval_stack.pop()
                    if token == '+':
                        eval_stack.push(operand1 + operand2)
                    elif token == '-':
                        eval_stack.push(operand1 - operand2)
                    elif token == '*':
                        eval_stack.push(operand1 * operand2)
                    elif token == '/':
                        eval_stack.push(operand1 / operand2)
                    elif token == '^' or token == '**':
                        eval_stack.push(operand1 ** operand2)

            return eval_stack.pop()

        # Вычисляем значение постфиксного выражения
        result = evaluate_postfix(postfix_expression)
        print("Результат:", result)
        self.previous_results.append((expression, postfix_str, result))
        return postfix_str, result

    def show_previous_results(self):
        print("//////////////////////// Результаты предыдущих вычислений")
        if not self.previous_results:
            print("Предыдущих результатов нет.")
        else:
            for idx, (expr, post_expr, result) in enumerate(self.previous_results, 1):
                print(f"{idx}. {expr} => {post_expr} = {result}")

    def run(self):
        while True:
            print("//////////////////////// Главное меню")
            print("Выберите:")
            print("1. Режим вычислений")
            print("2. Результаты предыдущих выражений")
            print("3. Выход")

            choice = input("Ваш выбор: ")

            if choice == '1':
                self.calculation_mode()
            elif choice == '2':
                self.show_previous_results()
            elif choice == '3':
                print("Выход.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def calculation_mode(self):
        print("//////////////////////// Режим вычислений")
        while True:
            print("Чтобы выйти в главное меню введите 'stop'.")
            expression = input("Введите выражение: ")
            if expression.lower() == 'stop':
                break
            self.infix_to_postfix_and_evaluate(expression)
            print(" ")

# Пример использования
calculator = Calculator()
calculator.run()
