import re
from reportlab.lib.colors import gray, HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

class DocumentGenerator:
    def __init__(self, file_path, document):
        self.file_path = file_path
        self.c = canvas.Canvas(self.file_path, pagesize=A4)
        self.width, self.height = A4
        self.margin = 12
        self.document = document
        self.fonts = self.document.fonts
        self.font_paths = self.document.font_paths
        self.font_sizes = self.document.font_sizes
        self.image_paths = self.document.image_paths

    def add_new_fonts(self, font, path):
        pdfmetrics.registerFont(TTFont(font, path))

    def draw_grid(self, page='light'):
        c, margin, width, height = self.c, self.margin, self.width, self.height
        num_lines = 13
        initial_ofset = 6 * margin
        additicional_ofset = 8
        margin_bottom = margin + 11
        line_spacing = 61.5

        # Header grid
        if page == 'light':
            c.setStrokeColorRGB(255, 0, 0, 0.3)
        else:
            c.setStrokeColorRGB(221, 221, 221, 0.3)

        c.setLineWidth(1)
        c.line(margin, height - margin, width - margin, height - margin)
        c.line(margin, height - (margin + 23), width - margin, height - (margin + 23))

        # Horizontal lines of the grid
        for i in range(num_lines):
            y_position = height - (initial_ofset + (i * line_spacing + additicional_ofset))
            c.line(margin, y_position, width - margin, y_position)
            c.line(margin, y_position + additicional_ofset, width - margin, y_position + additicional_ofset)

        # Vertical lines of the grid
        line_spacing = 47
        for i in range(num_lines):
            x_position = margin + i * line_spacing
            c.line(x_position, height - initial_ofset, x_position, margin_bottom)
            c.line(x_position + additicional_ofset, height - initial_ofset, x_position + additicional_ofset, margin_bottom)

    def draw_header(self, header_texts, color, page_number='01'):
        c, fonts, font_sizes, margin, width, height = self.c, self.fonts, self.font_sizes, self.margin, self.width, self.height
        circle_radius = 1
        text_y_position = height - margin - 15
        circle_y_position = height - margin - 12
        page_number_position = width - 3 * margin

        c.setFont(fonts['neue_montreal_medium'], font_sizes['small'])
        c.setStrokeColor(gray)
        c.setFillColor(gray)

        c.drawString(margin + 8, text_y_position, header_texts[0]['text'])
        c.circle(margin + 70, circle_y_position, circle_radius, fill=1, stroke=0)

        c.drawString(margin + 85, text_y_position, header_texts[1]['text'])
        c.circle(margin + 155, circle_y_position, circle_radius, fill=1, stroke=0)

        c.setFillColor(HexColor(color))
        c.drawString(margin + 170, text_y_position, header_texts[2]['text'])

        c.setStrokeColorRGB(0, 0, 0, 0.15)
        c.line(margin + 230, circle_y_position, margin + 525, circle_y_position)

        c.setFont(fonts['neue_montreal_medium'], 15)
        c.drawString(page_number_position, text_y_position - 2, page_number)

    def draw_subtitle(self, page='light'):
        c, height, margin, fonts, font_size = self.c, self.height, self.margin, self.fonts, self.font_sizes
        x_position = margin + 8
        y_position = height - margin - 81

        if page == 'light':
            c.setFillColorCMYK(0.00, 0.00, 0.00, 0.07)
        else:
            c.setFillColorCMYK(0.14, 0.03, 0.00, 0.21)

        c.rect(x_position, y_position, 94, 13, stroke=0, fill=1)
        c.setFont(fonts['neue_montreal_medium'], font_size['small'])
        c.setFillColor(HexColor("#233137"))
        c.drawString(x_position + 3.5, y_position + 3, "SEXUAL DIOMORPHISM")

    def draw_title(self, title, color):
        c, margin, height, fonts, font_sizes = self.c, self.margin, self.height, self.fonts, self.font_sizes
        x_position = margin + 8
        y_position = height - margin - 87
        column_width = 220
        custom_styles = ParagraphStyle(name='CustomStyle',
                                            fontName = fonts['neue_montreal_medium'],
                                            fontSize = font_sizes['large'],
                                            textColor = HexColor(color),
                                            leading = 45,
                                        )
        paragraph = Paragraph(title, custom_styles)
        _, h = paragraph.wrap(column_width, y_position)
        paragraph.drawOn(c, x_position, y_position - h)

    def draw_about(self, x, y, color, about):
        c, fonts, font_size = self.c, self.fonts, self.font_sizes
        c.setFont(fonts['zagma'], font_size['small'])
        c.setFillColor(gray)
        c.drawString(x, y, about[0])
        c.setFont(fonts['neue_montreal_medium'], font_size['normal'])
        c.setFillColor(HexColor(color))
        c.drawString(x + 20, y, about[1])

    def draw_text_columns(self):
        c, height, margin, fonts, font_size, document = self.c, self.height, self.margin, self.fonts, self.font_sizes, self.document
        ## Middle column and Right column - (Text continues in the next column)
        position_about_x = margin + 196
        position_about_y = height - margin - 100
        self.draw_about(position_about_x, position_about_y, '#121212', document.abouts[0])

        text = document.main_text
        paragraphs = re.split(r'<\/?p>', text) # Split text on <p></p> tags

        custom_styles = ParagraphStyle(name='CustomStyle',
                                            fontName = fonts['neue_montreal_thin'],
                                            fontSize = font_size['normal'],
                                            textColor = HexColor("#121212"),
                                            leading = 15,
                                            alignment = 4,
                                            wordWrap = 'LTR RTL',
                                        )

        paragraphs = [Paragraph(paragraph, custom_styles) for paragraph in paragraphs]

        column_width = 176
        column_height = 338

        x = margin + 196
        y = height - margin - 113

        for paragraph in paragraphs:
            _, height = paragraph.wrap(column_width, column_height)
            paragraph.drawOn(c, x, y - height)

            y -= height + 8 # Adjust the position for the next paragraph

            # If the remaining height in the column is not enough for the next paragraph, move to the next column
            if y < column_height:
                x += column_width + 15
                y = A4[1] - 125

    def draw_footer_imgs(self):
        c, width, height, margin, fonts, font_sizes, image_paths, img_legend = self.c, self.width, self.height, self.margin, self.fonts, self.font_sizes, self.image_paths, self.document.img_legend
        column_width = 180
        custom_styles = ParagraphStyle(name='CustomStyle',
                                            fontName = fonts['zagma'],
                                            fontSize = font_sizes['small'],
                                            textColor = gray,
                                            leading = 10,
                                        )
        paragraph = Paragraph(img_legend, custom_styles)

        _, h = paragraph.wrap(column_width, height - 752)
        paragraph.drawOn(c, margin + 8, height - 755 - h)

        c.drawImage(image_paths['image1'], x=(width - 397), y=(height - 809), width=200, height=175)
        c.drawImage(image_paths['image2'], x=(width - 199), y=(height - 809), width=179, height=175)

    def draw_second_page_column(self):
        c, height, margin, fonts, font_sizes, document = self.c, self.height, self.margin, self.fonts, self.font_sizes, self.document
        position_about_x = margin + 8
        position_about_y = height - margin - 244
        self.draw_about(position_about_x, position_about_y, '#FFFFFF', document.abouts[1])

        text = document.secondary_text
        column_width = 380
        x = position_about_x
        y = height - margin - 257
        custom_styles = ParagraphStyle(name='CustomStyle',
                                            fontName = fonts['neue_montreal_medium'],
                                            fontSize = font_sizes['medium'],
                                            textColor = HexColor('#FFFFFF'),
                                            leading = 20,
                                            firstLineIndent = 65
                                        )
        paragraph = Paragraph(text, custom_styles)
        _, h = paragraph.wrap(column_width, y)
        paragraph.drawOn(c, x, y - h)

    def draw_second_page_footer(self):
        c, width, height, margin, fonts, font_sizes, document = self.c, self.width, self.height, self.margin, self.fonts, self.font_sizes, self.document
        X_POSITION = margin + 8
        Y_POSITION = height - margin - 715

        c.setStrokeColorRGB(221, 221, 221, 0.3)
        c.line(X_POSITION, X_POSITION + 85, width - margin, X_POSITION + 85)
        c.line(X_POSITION, X_POSITION + 55, width - margin, X_POSITION + 55)
        c.line(X_POSITION, X_POSITION + 16, width - margin, X_POSITION + 16)

        footer_texts = document.footer_texts

        c.setFillColorRGB(221, 221, 221, 0.3)
        c.setFont(fonts['zagma'], font_sizes['normal'])

        x = [X_POSITION, X_POSITION + 189, X_POSITION + 375]
        y = Y_POSITION
        column_width = 190

        for i in range(len(footer_texts[0])):
            c.drawString(x[i], y, footer_texts[0][i])

        custom_styles = ParagraphStyle(name='CustomStyle',
                                        fontName = fonts['neue_montreal_thin'],
                                        fontSize = 9.6,
                                        textColor = HexColor('#FFFFFF'),
                                        leading = 12,
                                    )
        y -= 20

        for i in range(len(footer_texts[1])):
            paragraph = Paragraph(footer_texts[1][i], custom_styles)
            _, h = paragraph.wrap(column_width,  y)
            paragraph.drawOn(c, x[i],  y - h)

        y -= 30

        for i in range(len(footer_texts[2])):
            paragraph = Paragraph(footer_texts[2][i], custom_styles)
            _, h = paragraph.wrap(column_width,  y)
            paragraph.drawOn(c, x[i],  y - h)

    def generate_pdf(self):
        # Add new fonts
        self.add_new_fonts(self.fonts['neue_montreal_medium'], self.font_paths['neue_montreal_medium'])
        self.add_new_fonts(self.fonts['neue_montreal_thin'], self.font_paths['neue_montreal_thin'])
        self.add_new_fonts(self.fonts['zagma'], self.font_paths['zagma'])

        self.draw_grid() # Draw grid

        # Building content
        self.draw_header(self.document.headers_texts[0], '#121212')
        self.draw_subtitle()
        self.draw_title(self.document.titles[0], '#121212')
        self.draw_text_columns()
        self.draw_footer_imgs()

        self.c.showPage()

        # Draw background for the second page
        background_color = HexColor("#233137")
        self.c.setFillColor(background_color)
        self.c.rect(0, 0, self.width, self.height, fill=True)

        self.draw_grid('dark') # Draw grid

        # Building content for the second page
        self.draw_header(self.document.headers_texts[1], '#FFFFFF', page_number='02')
        self.draw_subtitle('dark')
        self.draw_title(self.document.titles[1], '#FFFFFF')
        self.draw_second_page_column()
        self.draw_second_page_footer()

        self.c.save()
