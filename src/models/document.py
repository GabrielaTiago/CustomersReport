class Document:
    font_paths = {
        'neue_montreal_medium': 'src/assets/fonts/montreal/ppneuemontreal-medium.ttf',
        'neue_montreal_thin': 'src/assets/fonts/montreal/ppneuemontreal-thin.ttf',
        'zagma': 'src/assets/fonts/F37Zagma/F37ZagmaMonoTrial-Regular.ttf'
    }
    fonts = {
        'neue_montreal_medium': 'NeueMontrealMedium',
        'neue_montreal_thin': 'NeueMontrealThin',
        'zagma': 'Zagma'
    }
    font_sizes = {
        'small': 8,
        'normal': 10,
        'medium': 20,
        'large': 40
    }
    headers_texts = [
        (
            {'text': 'Preliminary'},
            {'text': 'Dimorphism'},
            {'text': 'Theory'}
        ),
        (
            {'text': 'Preliminary'},
            {'text': 'Dimorphism'},
            {'text': 'Assessment'},
        )
    ]
    titles = ['Theory', 'Assessment Overview']
    abouts = [ ('01/', 'What Is It?'), ('02/', 'Next Fwe Pages')]
    image_paths = {
        'image1': 'src/assets/imgs/img-1.jpg',
        'image2': 'src/assets/imgs/img-2.jpg',
    }
    footer_texts = [
        ('TABLE III', 'RAW RESULT','EXPLANATION'),
        ('Euclidean Matrix Analysis', 'Saller and colleagues <sup>[22]</sup>', 'The subject has a moderately juvenile face.'),
        ('Dimorphism Analysis', 'Edmondson and colleagues <sup>[23]</sup>', 'Measuring changes of the face as as masculinity is artificially increased or decreased')
    ]

    def __init__(self, main_text, img_legend, secondary_text):
        self.main_text = main_text
        self.img_legend = img_legend
        self.secondary_text = secondary_text

def get_document():
    text1 = '''
        <p>Humans have long been fascinated by facial proportions as ultimately these proportions make up the geometry of one’s face. In short, you are your proportions, measurements and ratios.</p>
        <p>Following this, it is easy to understand why proportions are so closely linked to beauty. An attractive face by definition would have to have different proportions to an unattractive one as they inherently look different and have different forms. While this idea has held true for millennia, our application of facial proportions has changed.</p>
        <p>In the early BC years, Ancient Greeks believed in divine proportions and canons of beauty. Think of the ‘Golden Ratio’, ‘Perfect Thirds,’ or similar and we can link them back to the works of early Hellenistic philosophers. In fact, most famous renaissance works such as Michalengo’s ‘David’ statue followed these proportions of beauty..</p>
        <p>However, modern science shows us these proportions of beauty are misguided. They are simply too idealistic to be realistic. Schmid Et al’s research found only a weak link between these Golden Ratios and Neoclassical canons, meaning they are not as closely linked to beauty as humans once thought.
        <p>Instead, in contemporary science, plastic surgeons and orthodontists use ‘Modern Anthropometry,’ where instead of relying on arbitrary proportions and one-size-fits-all shapes, we use demographic data of populations to establish the actual proportions that contribute to attractiveness for that group.</p>
        <p>For example, the features that makes a <font color="#233137"><u>White Male</u></font> of <font color="#233137"><u>30 years age</u></font> attractive, may not necessarily be the same proportions that make a <font color="#233137"><u>Black Woman</u></font> of <font color="#233137"><u>20 years age</u></font> attractive, which is why Modern Anthropometry is needed. Clincians must compare apples to apples to be precise.</p>
    '''
    img_l = 'FIG 2 : Ratios greater than 1.10 (i.e. there is a 110% difference between you and the most extreme comparisons) are shown here as they are dimorphic traits.'
    text2 = 'Our main goal with Facial Proportions is to take an overall look at your facial configuration and dimensions. Later in chapter 2 we look into individual proportions, feature-by-feature.'
    return Document(text1, img_l, text2)