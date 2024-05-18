
from math import sqrt

class Model:
    
    # cuz that is how calculators operate
    clear_on_next_action = False
    can_switch_operator = False

    def __init__(self):
        self.value = ''
        self.previous_value = ''
        self.operator = ''


    def _append_number(self, number):
        if self.clear_on_next_action:
            self.value = ''
            self.clear_on_next_action = False

        if self.value == '0' and number == 0:
            return
        if self.value == '0' and not number == 0:
            self.value = ''
        self.value += str(number)


    def _finalize(self):
        match self.operator:
            case '÷':
                if self.value == '0':
                    return
                self.value = str( float(self.previous_value) / float(self.value) )
            case '*':
                self.value = str( float(self.previous_value) * float(self.value) )
            case '-':
                self.value = str( float(self.previous_value) - float(self.value) )
            case '+':
                self.value = str( float(self.previous_value) + float(self.value) )
            case _:
                print("How")
                self.value = str( float(self.previous_value) + float(self.value) )

        self.clear_on_next_action = True
        self.can_switch_operator = False
        self.previous_value = ''
        self.operator = ''


    def calculate(self, caption):
        if self.can_switch_operator and caption not in ('÷','*','-','+'):
            self.can_switch_operator = False
        match caption:
            case num if num in range(0,10):
                self._append_number(caption)
            # Global clear - clear the entire calculation
            case 'C':
                self.value = ''
                self.previous_value = ''
                self.operator = ''
                self.clear_on_next_action = False
                self.can_switch_operator = False
            case 'CE':
                self.value = ''
            case '.':
                if not '.' in self.value:
                    if self.value == '':
                        self.value = '0'
                    self.value += '.'
            
            case '+/-':
                if self.value[0] == '-':
                    self.value = self.value[1:]
                else:
                    self.value = '-' + self.value
            case '⌫':
                self.value = self.value[:-1]
            
            
            case '1/x':
                self.value = str(1 / float(self.value))
                self.clear_on_next_action = True
            case 'x²':
                self.value = str(float(self.value) * float(self.value))
                self.clear_on_next_action = True
            case '√x':
                self.value = str(sqrt(float(self.value)))
                self.clear_on_next_action = True

            case '%':
                if not self.previous_value == '':
                    self.value = str(float(self.previous_value) * float(self.value) * 0.01)
            case operator if operator in ('÷','*','-','+'):
                if self.can_switch_operator:
                    self.operator = operator
                else:
                    if self.previous_value == '':
                        self.operator = operator
                        self.previous_value = self.value
                        self.value = ''
                        self.can_switch_operator = True
                    elif not self.value == '':
                        self._finalize()

            case '=':
                if not self.previous_value == '' and not self.value == '':
                    self._finalize()
                self.clear_on_next_action = True


            case _:
                print(f'Button {caption}')
        
        #print(self.operator, self.can_switch_operator, self.previous_value)
        return self.value
