from flask import Flask, request, jsonify

application = Flask(__name__)

SPACE = ':empty:'
EMOJI = ':janne:'
GAP = '   '

characters = {
    'A': [
      '00100',
      '01010',
      '01010',
      '11111',
      '10001'
    ],
    'B': [
      '1100',
      '1010',
      '1111',
      '1001',
      '1110'
    ],
    'C': [
      '011',
      '100',
      '100',
      '100',
      '011'
    ],
    'D': [
      '1110',
      '1001',
      '1001',
      '1001',
      '1110'
    ],
    'E': [
      '1111',
      '1000',
      '1110',
      '1000',
      '1111'
    ],
    'F': [
      '111',
      '100',
      '110',
      '100',
      '100'
    ],
    'G': [
      '0111',
      '1000',
      '1011',
      '1001',
      '0111'
    ],
    'H': [
      '1001',
      '1001',
      '1111',
      '1001',
      '1001'
    ],
    'I': [
      '1',
      '1',
      '1',
      '1',
      '1'
    ],
    'J': [
      '001',
      '001',
      '001',
      '101',
      '011'
    ],
    'K': [
      '1001',
      '1010',
      '1100',
      '1011',
      '1001'
    ],
    'L': [
      '100',
      '100',
      '100',
      '100',
      '111'
    ],
    'M': [
      '10001',
      '11011',
      '10101',
      '10001',
      '10001'
    ],
    'N': [
      '1001',
      '1101',
      '1011',
      '1001',
      '1001'
    ],
    'O': [
      '0110',
      '1001',
      '1001',
      '1001',
      '0110'
    ],
    'P': [
      '1110',
      '1001',
      '1111',
      '1000',
      '1000'
    ],
    'Q': [
      '0110',
      '1001',
      '1001',
      '1010',
      '0101'
    ],
    'R': [
      '1110',
      '1001',
      '1111',
      '1010',
      '1001'
    ],
    'S': [
      '0111',
      '1000',
      '1111',
      '0001',
      '1110'
    ],
    'T': [
      '111',
      '010',
      '010',
      '010',
      '010'
    ],
    'U': [
      '1001',
      '1001',
      '1001',
      '1001',
      '0111'
    ],
    'V': [
      '10001',
      '10001',
      '01010',
      '01010',
      '00100'
    ],
    'W': [
      '10001',
      '10001',
      '10101',
      '10101',
      '01010'
    ],
    'X': [
      '10001',
      '01010',
      '00100',
      '01010',
      '10001'
    ],
    'Y': [
      '10001',
      '01010',
      '00100',
      '00100',
      '00100'
    ],
    'Z': [
      '1111',
      '0001',
      '0010',
      '0100',
      '1111'
    ],
}


@application.route('/', methods=['POST'])
def jannefy():
    text = request.form['text']
    outputs = []

    for c in text:
        if c.upper() not in characters:
            return jsonify({
                'response_type': 'ephemeral',
                'text': 'Only characters a-z are supported.'
            })

    representations = [characters[c.upper()] for c in text]
    for i in range(len(characters['A'])):
        output = ''
        for representation in representations:
            line = representation[i].replace('1', EMOJI)
            line = line.replace('0', SPACE)
            line += GAP

            output += line

        outputs.append(output)

    return jsonify({
        'response_type': 'in_channel',
        'text': '\n'.join(outputs)
    })


if __name__ == '__main__':
    application.run(host='0.0.0.0')
