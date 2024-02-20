# Customers Report

This project aims to build two pages in ReportLab programmatically. The pages will be built inside a class object, where each class instance represents a Customer's Report with its own handling of states, data, etc.

## Task Description

The task involves the following requirements:

1. Build the two pages using ReportLab.
2. The pages should be built inside a class object.
3. Each class instance represents a Customer's Report.
4. All text can be hardcoded directly within the class as these are static pages.
5. For Task 1, the two paragraphs must be split such that no matter how long the paragraph is, they are split mostly evenly across the two columns.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository.
   `git clone https://github.com/GabrielaTiago/CustomersReport.git`
2. Install the required dependencies.
   `pip install -r requirements.txt`
3. Run the main script to generate the Customer's Report.

## Dependencies

This project requires the following dependencies:

- ReportLab: [Link to ReportLab](https://www.reportlab.com/)

## Structure

```markdown
├── src/
│ ├── assets/
│ │ ├── fonts/
│ │ │ ├── F37Zagma/
│ │ │ └── montreal/
│ │ └── imgs/
│ │
│ ├── controller/
│ │ ├── init.py
│ │ └── document_controller.py
│ │
│ ├── model/
│ │ ├── init.py
│ │ └── document.py
│ │
│ ├── view/
│ │ ├── init.py
│ │ └── document_view.py
│ │
│ └── main.py
│
├── .gitignore
├── document.pdf
├── README.md
└── requirements.txt
```

## Results

- PDF with the grid off

<div style="display: flex;">
    <div style="flex: 50%; padding: 5px;">
        <img src="src/assets/imgs/result_imgs/3.png" alt="page 1 pdf" width="100%">
    </div>
    <div style="flex: 50%; padding: 5px;">
        <img src="src/assets/imgs/result_imgs/4.png" alt="page 2 pdf" width="100%">
    </div>
</div>

- PDF with the grid on

<div style="display: flex;">
    <div style="flex: 50%; padding: 5px;">
        <img src="src/assets/imgs/result_imgs/1.png" alt="page 1 pdf grid on" width="100%">
    </div>
    <div style="flex: 50%; padding: 5px;">
        <img src="src/assets/imgs/result_imgs/2.png" alt="page 2 pdf grid on" width="100%">
    </div>
</div>
