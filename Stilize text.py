import random
import pyperclip

# Alternative Unicode styles for different letters, numbers, and punctuation marks
char_styles = {
    "A": ["𝓐", "𝐀", "𝔄", "𝙰", "𝕬", "𝖠", "𝒜", "🅐", "🅰"],
    "B": ["𝓑", "𝐁", "𝔅", "𝙱", "𝕭", "𝖡", "🅑", "🅱"],
    "C": ["𝓒", "𝐂", "𝙲", "𝕮", "𝖢", "🅒", "🅲"],
    "Ç": ["Ç", "𝓒̧", "𝐂̧", "𝙲̧", "ℂ̧"],
    "D": ["𝓓", "𝐃", "𝔇", "𝙳", "𝕯", "𝖣", "🅓", "🅳"],
    "E": ["𝓔", "𝐄", "𝔈", "𝙴", "𝕰", "𝖤", "🅔", "🅴"],
    "F": ["𝓕", "𝐅", "𝔉", "𝙵", "𝕱", "𝖥", "🅕", "🅵"],
    "G": ["𝓖", "𝐆", "𝔊", "𝙶", "𝕲", "𝖦", "🅖", "🅶"],
    "Ğ": ["Ğ", "𝓖̆", "𝐆̆", "𝙶̆", "𝖦̆", "🅖̆"],
    "H": ["𝓗", "𝐇", "🅗","Ḫ","🄷","ℋ","ℍ"],
    "I": ["𝓘", "𝐈", "🅘", "🅸","Ɪ","🄸","𝕀"],
    "İ": ["İ","Ị","⒤","Ĭ","Î"],
    "J": ["𝓙", "𝐉", "𝔍", "𝙹", "𝕵", "𝖩", "🅙"],
    "K": ["𝓚", "𝐊", "𝔎", "𝙺", "𝕶", "𝖪", "🅚", "🅺"],
    "L": ["𝓛", "𝐋", "𝔏", "𝙻", "𝕷", "𝖫", "🅛", "🅻"],
    "M": ["𝓜", "𝐌", "𝔐", "𝙼", "𝕸", "𝖬", "🅜", "🅼"],
    "N": ["𝓝", "𝐍", "𝔑", "𝙽", "𝕹", "𝖭", "🅝", "🅽"],
    "O": ["𝓞", "𝐎", "𝔒", "𝙾", "𝕺", "𝖮", "🅞", "🅾️"],
    "Ö": ["Ö", "𝓞̈", "𝐎̈", "𝙊̈", "🅞̈"],
    "P": ["𝓟", "𝐏", "𝔓", "𝙿", "𝕻", "𝖯", "🅟", "🅿️"],
    "Q": ["𝓠", "𝐐", "𝔔", "𝚀", "𝕼", "𝖰", "🅠", "🅀"],
    "R": ["𝓡", "𝐑", "🅡","𝕽","₹","Ṛ","Ⓡ","ᚱ","Ṙ"],
    "S": ["𝓢", "𝐒", "𝔖", "𝚂", "𝕾", "𝖲", "🅢", "🅂"],
    "Ş": ["Ş", "𝓢̧", "𝐒̧", "𝚂̧","Ṩ","Ȿ"],
    "T": ["𝓣", "𝐓", "𝔗", "𝚃", "𝕿", "𝖳", "🅣"],
    "U": ["𝓤", "𝐔", "𝔘", "𝚄", "𝖀", "𝓤̈", "𝐔̈", "𝙐̈"],
    "Ü": ["Ü","Ṻ","Ů","Ȕ","Ǖ"],
    "V": ["𝓥", "𝐕", "𝚅", "🅥"],
    "W": ["𝓦", "𝐖", "𝔚", "𝚆", "𝖂", "𝒲", "🅦"],
    "X": ["𝓧", "𝐗", "𝔛", "𝚇", "𝖃", "𝒳", "🅧", "❌"],
    "Y": ["𝓨", "𝐘", "𝔜", "𝚈", "𝖄", "𝒴", "🅨"],
    "Z": ["𝓩", "𝐙", "🅩","Ⓩ","ⓩ","ℤ","Ƶ","Ẕ","Ż"],
    "ı": ["ı", "𝚒", "𝐢", "𝔦"],
    "i": ["𝓲", "𝐢", "𝔦", "𝚒", "𝖎","⒤","ⓘ","ï"],
    "o": ["𝓸", "𝐨", "𝔬", "𝚘", "𝖔"],
    "u": ["𝓾", "𝐮", "𝔲", "𝚞", "𝖚"],
    "0": ["𝟘", "𝟬", "𝟬", "𝟘","🄋","߀"],
    "1": ["𝟙", "𝟭", "𝟣", "𝟙","Ⅰ","①"],
    "2": ["𝟚", "𝟮", "𝟤", "𝟚","Ⅱ","②"],
    "3": ["𝟛", "𝟯", "𝟧", "𝟛","Ⅲ","⑶"],
    "4": ["𝟜", "𝟰", "𝟨", "𝟜","Ⅳ","⁴"],
    "5": ["𝟝", "𝟱", "𝟩", "𝟝","Ⅴ","➎"],
    "6": ["𝟞", "𝟲", "𝟪", "𝟞","Ⅵ","₆"],
    "7": ["𝟟", "𝟳", "𝟫", "𝟟","Ⅶ","➆"],
    "8": ["𝟠", "𝟴", "𝟬", "𝟠","Ⅷ","⒏"],
    "9": ["𝟡", "𝟵", "𝟭", "𝟡","Ⅸ","⒐"],
    "10": ["𝟙𝟘","１０","𝟏𝟎","Ⅹ","⑽","㉈"],
    ",": ["，", "٫"],
    ".": [".", "•","✦","◍","◎","⦿","。"],
    "?": ["¿", "⸮", "⁇","🧐", "❓"],
    "!": ["❗", "‼", "❕","❣","⚠","ꜝ"],
    "-": ["⸗", "−", "‐", "₋"],
    ":": ["∶","⁚", "⁑","⦂"],
    ";": ["﹕", "⁏", "﹔"]
}

# Function to stylize the text
def stylize_text(text):
    styled_text = ""
    for char in text:
        if char.upper() in char_styles:
            styled_text += random.choice(char_styles[char.upper()])
        else:
            styled_text += char  # If no special style exists, leave the character as is
    return styled_text

# Stylize the main text and copy it to the clipboard
def main():
    original_text = input("Text to be stylised: ")
    
    while True:
        # Stylize the text
        styled_text = stylize_text(original_text)

        # Print the stylized text
        print(f"Stylized text: {styled_text}")

        # Copy the text to the clipboard
        pyperclip.copy(styled_text)
        print("Text copied to clipboard.")

        # Wait for Enter to generate a new text
        input("Press Enter to generate a new text (press Ctrl+C to exit)...")

if __name__ == "__main__":
    main()
