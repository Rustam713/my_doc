text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""

# Напишите функцию, которая берет текст, и возвращает строковое значение, состоящее из заглавных букв.
# Используйте текст, данный выше (The Zen of Python).
# Подсказка: используйте метод строчных значений, который проверяет, “заглавность” буквы.


print(text)
text_big = []
def is_upper():
    for i in text:
        
        if i.isupper():
            text_big.append(i)

        else:
            continue                    

    text_big1 = ''.join(text_big)
    print(text_big1)
is_upper()











