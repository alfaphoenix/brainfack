import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def welcom(message):
    bot.send_message(message.chat.id, 'привет,ты полный мазахист раз оказался здесь')

@bot.message_handler(content_types='text')
def brainfack(message):
    def block(code):
        opened = []
        blocks = {}
        for i in range(len(code)):
            if code[i] == '[':
                opened.append(i)
            elif code[i] == ']':
                blocks[i] = opened[-1]
                blocks[opened.pop()] = i
        return blocks

    def parse(code):
        return ''.join(c for c in code if c in '><+-.,[]')

    def run(code):
        chars = ''
        code = parse(code)
        x = i = 0
        bf = {0: 0}
        blocks = block(code)
        l = len(code)
        while i < l:
            sym = code[i]
            if sym == '>':
                x += 1
                bf.setdefault(x, 0)
            elif sym == '<':
                x -= 1
            elif sym == '+':
                bf[x] += 1
            elif sym == '-':
                bf[x] -= 1
            elif sym == '.':
                a = chr(bf[x])
                chars += a
#данная функция пока не работает
            elif sym == ',':
                bf[x] = int(input('Input: '))
            elif sym == '[':
                if not bf[x]: i = blocks[i]
            elif sym == ']':
                if bf[x]: i = blocks[i]
            i += 1
        return chars
    code = message.text
    if '.' in code:
        bot.send_message(message.chat.id, run(code))
    else:
        pass


bot.polling()