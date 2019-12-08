# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:33:57 2019

@author: Марьяша
"""

questions = [
        [
                "What is the difference between “carat” and “karat”?",
                ['There is no difference', 'A carat is a unit of weight used to measure the size of a gemstone such as a diamond. A karat is a measurement indicating the proportion of gold in an alloy out of 24 parts', '“Carat” is an English way of spelling and “karat” – Norwegian'],
                'A carat is a unit of weight used to measure the size of a gemstone such as a diamond. A karat is a measurement indicating the proportion of gold in an alloy out of 24 parts',
        ],
                
        #
        [
                "How many grams is a 1 carat diamond?",
                ['0.02 grams', '1.2 grams', '0.2 grams'],
                '0.02 grams',
        ],
                
                        #
        [
                "What is the size of 1 carat diamond?",
                ['5.7 mm', '5 mm', '6.5 mm'],
                '6.5 mm',
        ],
    
        [
                "In gemology gem hardness is measured on a scale known as:",
                ['the Marcels’ scale', 'the Mocks’ scale', 'the Mohs’ scale'],
                'the Mohs’ scale',
        ],
                
        [
                "Which primary gem varieties has corundum?",
                ['sapphire and emerald', 'ruby and sapphire', 'emerald and aquamarine'],
                'ruby and sapphire',
        ],
                
        #
        [
                "Which mineral has a hardness of 1 according to the Mohs’ scale?",
                ['gypsum', 'calcite', 'talc'],
                'talc',
        ],
                
                        #
        [
                "What is a diameter of a ring if the size is 56?",
                ['17,83 mm', '16 mm', '18,47 mm'],
                '17,83 mm',
        ],
    
        [
                "What is the melting point of pure silver?",
                ['961 °C', '1084 °C', '1063 °C'],
                '961 °C',
        ],
                
        [
                "Can white gold be found in nature?",
                ['yes', 'no'],
                'no',
        ],
                
                        #
        [
                "Sterling silver is:",
                ['an alloy of silver containing 92.5 % by weight of silver and 7.5 % by weight of other metals', 'a chemical element with the symbol Ag', 'an alloy of silver containing 83 % by weight of silver and 17 % by weight of other metals'],
                'an alloy of silver containing 92.5 % by weight of silver and 7.5 % by weight of other metals',
        ],
    
        [
                "What is percent of pure gold in 18k yellow gold?",
                ['80 %', '75 %', '58,3 %'],
                '75 %',
        ],
                
        [
                "What are the symbols for silver, gold and platinum in the periodic table?",
                ['Ag, Au,  Pt', 'Ag, Gd, Pa', 'Au, Gd, Pu'],
                'Ag, Au,  Pt',
        ],
                
        #
        [
                "The four Cs of diamond grading stands for:",
                ['carat, cut, color and certification', 'carat, clarity, color, and cut', 'carat, clarity, class and cut'],
                'carat, clarity, color, and cut',
        ],
                
                        #
        [
                "2020 is the year of:",
                ['Earth Pig', 'Metal Rat', 'Red Rat'],
                'Metal Rat',
        ],
    
      
]

if __name__ == '__main__':

    points = 0

    for question_info in questions:

        #question, options, correct = question_info
        question = question_info[0]
        options = question_info[1]
        correct = question_info[2]
        
        print(question)
        print()
        
        for number, option in enumerate(options):
            print(f'\t{number+1}: {option}')
        
        guess = input()
        
        correct_option = options.index(correct)+1
        
        if guess == str(correct_option):
            points = points + 1
            print('Correct! Score is: ', points)
        else:
            print(f'Incorrect answer. Correct was {correct_option}: {correct}')

