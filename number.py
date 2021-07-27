

def main():
    print("Plz Attenction bodmas method not support for this script..!")
    try:
        userInput = input(" > ")
    except:
        quit()
    userInputData = userInput.split()
    count = 1
    for i in userInputData:
        if count % 2 == 1:
            try:
                int(i)
            except Exception as err:
                print(err)
                quit()
        else:
            if not i in ['/','*','+','-']:
                print('Something Wrong')
                quit()
        count += 1
    run = 1
    try:
        choice = int(input('''
            Input data :
                [1] base10
                [2] base2
        >> '''))
        if choice == 1:
            pass
        elif choice == 2: 
            Convert2(userInputData)
        else:
            print('Error..!')
            run = 0
    except ValueError:
        print('Error..!')
        run = 0
    except KeyboardInterrupt:
        quit()
    if run == 1:
        data = Convert(userInputData)
        value = getvalue(data)
        answer = getAnswer(value)
        for i in answer:
            print(f'base{i} = {answer[i]}')  
    else:
        pass  


def getAnswer(data):
    hexcode = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    Answ2 = ''
    Answ8_ = ''
    Answ10_ = data
    Answ16_ = ''
    #2
    binary = data
    while binary != 0:
        if binary % 2 == 0:
            Answ2 = f'0{Answ2}'
        else:
            Answ2 = f'1{Answ2}'
        binary = binary // 2 
    #8
    base8 = data
    while base8 != 0:
        Answ8 = base8 % 8
        if not base8 == 0 :   
            Answ8_ = f'{Answ8}{Answ8_}'
            base8 = base8 // 8
    #16
    base16 = data
    while base16 != 0:
        Answ16 = base16 % 16
        if not base16 == 0 : 
            Answ16_ = f'{hexcode[Answ16]}{Answ16_}'
            base16 = base16 // 16
    return {2:Answ2,8:Answ8_,10:Answ10_,16:Answ16_}


def getvalue(data):
    for i in range(len(data)):  
        try:
            if i == 0:
                value1 = data[i]
                value2 = data[i*2+1]
                value3 = data[i*2+2]
            else:
                value2 = data[i*2+1]
                value3 = data[i*2+2]
            if value2 == "+":
                value1 = value1 + value3
            elif value2 == "-":
                value1 = value1 - value3
            elif value2 == "*":
                value1 = value1 * value3
            elif value2 == "/":
                value1 = value1 / value3
            else:
                print(value2)
            if '.' in str(value1) and  str(value1)[-2:] != '.0':
                print('some error..! #float')
                print(value1)
                quit()
            value1 = int(value1)
        except Exception as err:
            pass
    return value1;


def Convert(data):
    for i in range (len(data)):
        if not i % 2 == 1 :
            data[i] = int(data[i])
    return data;

def Convert2(data):
    for i in range(len(data)):
        if i % 2 != 1:
            sum = 0
            #print(data[i])
            #print(len(str(data[i])))
            for ii in range(len(str(data[i]))):
                num = int(data[i][(ii+1)*-1])
                power = f'2  {ii}'
                #print(f'ii = {ii}, postion - {[(ii+1)*-1]}')
                #print(num,power)
                sum += int(data[i][(ii+1)*-1]) * 2 ** ii
            #print(sum)
            data[i] = sum
    return data;



           

if __name__ == '__main__':
    try :
        while True:
            main()
    except Exception as err:
        print(err)
        quit()