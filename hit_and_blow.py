import PySimpleGUI as sg
import random

layout = [
    [

        sg.Menu([
                ['File', [
                    'NEW',
                    'EXIT'
                ]]
                ])

    ],
    [
        sg.Text('HIT :', size=(6, 1)),
        sg.Input('0', key='-HIT-', size=(3, 1), readonly=True),
        sg.Text('BLOW :', size=(6, 1)),
        sg.Input('0', key='-BLOW-', size=(3, 1), readonly=True),
        sg.Text('TURN :', size=(6, 1)),
        sg.Input('0', key='-TURN-', size=(3, 1), readonly=True),
    ],

    [
        sg.Text('YOUR ANSWER'),
        sg.Input('1234', key='-INPUT-', size=(10, 1)),
        sg.Button('PUSH', key='-PUSH-', size=(5, 1))
    ],

]


window = sg.Window('HIT AND BLOW', layout)
window.finalize()


def create_new_number():
    nums = list(range(10))
    window['-TURN-'].update(0)
    return(random.sample(nums, 4), 0)


def hit_and_blow(input_nums, target):
    print("PUSH")
    hit = 0
    blow = 0
    for i in range(len(input_nums)):
        if input_nums[i] == target[i]:
            hit += 1
        else:
            if input_nums[i] in target:
                blow += 1
    print("Hit=", hit, "Blow=", blow)
    window['-HIT-'].update(hit)
    window['-BLOW-'].update(blow)
    if hit == 4:
        sg.popup("YOU WIN")


target, turn = create_new_number()
print("target=", target)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-PUSH-':
        if values['-INPUT-'] == '':
            print('ERROR NONE')
        elif 0 <= int(values['-INPUT-']) < 10000:
            input_nums = []
            for i in values['-INPUT-']:
                input_nums.append(int(i))
            print("input=", input_nums)
            set_input_nums = set(input_nums)
            if len(set_input_nums) == len(input_nums):
                turn += 1
                hit_and_blow(input_nums, target)
                window['-TURN-'].update(turn)
            else:
                print("duplicate numbers")

        else:
            print('ERROR')
    if event == 'NEW':
        target, turn = create_new_number()
        print("target=", target)

window.close()
