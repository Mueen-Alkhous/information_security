from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTabWidget, QTextEdit, QHBoxLayout, QMessageBox
from algorithms import caesar
from algorithms import affine
from algorithms import hill
from algorithms import affine_hill
import numpy as np

class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Ciphering App")
        self.setGeometry(100, 100, 600, 400)

        # Create the tab widget
        self.tab_widget = QTabWidget()
        
        # Create tabs for each cipher algorithm
        self.tab_caesar = self.create_caesar_tab()
        self.tab_affine = self.create_affine_tab()
        self.tab_hill = self.create_hill_tab()
        self.tab_affine_hill = self.create_affine_hill_tab()
        self.tab_vigenere = self.create_vigenere_tab()

        # Add tabs to the widget
        self.tab_widget.addTab(self.tab_caesar, "Caesar Cipher")
        self.tab_widget.addTab(self.tab_affine, "Affine Cipher")
        self.tab_widget.addTab(self.tab_hill, "Hill Cipher")
        self.tab_widget.addTab(self.tab_affine_hill, "Affine-Hill")
        self.tab_widget.addTab(self.tab_vigenere, "Vigenere")

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)

        self.setLayout(main_layout)


    def create_caesar_tab(self):
        # Create Caesar cipher tab
        tab = QWidget()
        layout = QVBoxLayout()

        # Input field for plain text
        self.caesar_input = QTextEdit()
        self.caesar_input.setPlaceholderText("Enter text to encrypt/decrypt...")
        
        # Input for shift
        self.caesar_shift = QLineEdit()
        self.caesar_shift.setPlaceholderText("Enter shift value...")

        

        # Output field for ciphered text
        self.caesar_output = QTextEdit()
        self.caesar_output.setPlaceholderText("Encrypted/Decrypted text will appear here...")
        self.caesar_output.setReadOnly(True)

        two_buttens_layout = QHBoxLayout()

        # Button to cipher the text
        encrypt_button = QPushButton("Encrypt")
        encrypt_button.clicked.connect(self.caesar_cipher_action)

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.caesar_cipher_action)

        two_buttens_layout.addWidget(encrypt_button)
        two_buttens_layout.addWidget(decrypt_button)

        layout.addWidget(QLabel("Caesar Cipher"))
        layout.addWidget(self.caesar_input)
        layout.addWidget(self.caesar_shift)
        layout.addLayout(two_buttens_layout)
        layout.addWidget(self.caesar_output)

        tab.setLayout(layout)
        return tab

    def create_affine_tab(self):
        # Create Affine cipher tab
        tab = QWidget()
        layout = QVBoxLayout()

        # Input field for plain text
        self.affine_input = QTextEdit()
        self.affine_input.setPlaceholderText("Enter text to cipher...")

        # Inputs for a and b coefficients
        self.affine_a = QLineEdit()
        self.affine_a.setPlaceholderText("Enter 'a' value...")

        self.affine_b = QLineEdit()
        self.affine_b.setPlaceholderText("Enter 'b' value...")

        # Output field for ciphered text
        self.affine_output = QTextEdit()
        self.affine_output.setPlaceholderText("Ciphered text will appear here...")
        self.affine_output.setReadOnly(True)

        # Button to cipher the text
        encrypt_button = QPushButton("Encrypt")
        encrypt_button.clicked.connect(self.affine_cipher_action)

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.affine_cipher_action)

        two_buttons_layout = QHBoxLayout()
        two_buttons_layout.addWidget(encrypt_button)
        two_buttons_layout.addWidget(decrypt_button)

        layout.addWidget(QLabel("Affine Cipher"))
        layout.addWidget(self.affine_input)
        layout.addWidget(self.affine_a)
        layout.addWidget(self.affine_b)
        layout.addLayout(two_buttons_layout)
        layout.addWidget(self.affine_output)

        tab.setLayout(layout)
        return tab

    def create_hill_tab(self):
        # Create Hill cipher tab
        tab = QWidget()
        layout = QVBoxLayout()

        # Input field for plain text
        self.hill_input = QTextEdit()
        self.hill_input.setPlaceholderText("Enter text to cipher...")

        # Input for matrix
        self.hill_matrix = QTextEdit()
        self.hill_matrix.setPlaceholderText("Enter matrix values row by row (comma-separated)...")

        # Output field for ciphered text
        self.hill_output = QTextEdit()
        self.hill_output.setPlaceholderText("Ciphered text will appear here...")
        self.hill_output.setReadOnly(True)

        # Button to cipher the text
        encrypt_button = QPushButton("Encrypt")
        encrypt_button.clicked.connect(self.hill_cipher_action)

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.hill_cipher_action)

        two_buttons_layout = QHBoxLayout()
        two_buttons_layout.addWidget(encrypt_button)
        two_buttons_layout.addWidget(decrypt_button)

        layout.addWidget(QLabel("Hill Cipher"))
        layout.addWidget(self.hill_input)
        layout.addWidget(QLabel("Enter Matrix:"))
        layout.addWidget(self.hill_matrix)
        layout.addLayout(two_buttons_layout)
        layout.addWidget(self.hill_output)

        tab.setLayout(layout)
        return tab

    def create_affine_hill_tab(self):
        # Create Hill cipher tab
        tab = QWidget()
        layout = QVBoxLayout()

        # Input field for plain text
        self.affine_hill_input = QTextEdit()
        self.affine_hill_input.setPlaceholderText("Enter text to cipher...")

        # Input for matrices
        self.matrices_layout = QHBoxLayout()

        self.A_matrix = QTextEdit()
        self.A_matrix.setPlaceholderText("Enter matrix A values row by row (comma-separated)...")

        self.B_matrix = QTextEdit()
        self.B_matrix.setPlaceholderText("Enter matrix B values row by row (comma-separated)...")

        self.matrices_layout.addWidget(self.A_matrix)
        self.matrices_layout.addWidget(self.B_matrix)

        # Output field for ciphered text
        self.affine_hill_output = QTextEdit()
        self.affine_hill_output.setPlaceholderText("Ciphered text will appear here...")
        self.affine_hill_output.setReadOnly(True)

        # Button to cipher the text
        self.two_buttons_layout = QHBoxLayout()

        encrypt_button = QPushButton("Encrypt")
        encrypt_button.clicked.connect(self.affine_hill_cipher_action)

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.affine_hill_cipher_action)

        self.two_buttons_layout.addWidget(encrypt_button)
        self.two_buttons_layout.addWidget(decrypt_button)

        layout.addWidget(QLabel("Affine-Hill Cipher"))
        layout.addWidget(self.affine_hill_input)
        layout.addWidget(QLabel("Enter Matrix:"))
        layout.addLayout(self.matrices_layout)
        layout.addLayout(self.two_buttons_layout)
        layout.addWidget(self.affine_hill_output)

        tab.setLayout(layout)
        return tab


    def caesar_cipher_action(self):
        # Placeholder action for Caesar cipher
        text = self.caesar_input.toPlainText()
        shift = int(self.caesar_shift.text())
        cipher = caesar.caesar_cipher(text, shift, self.sender().text().lower())
        self.caesar_output.setPlainText(f"{cipher}")

    def affine_cipher_action(self):
        # Placeholder action for Affine cipher
        text = self.affine_input.toPlainText()
        a = int(self.affine_a.text())
        b = int(self.affine_b.text())
        if affine.gcd(a, 26) != 1:
            QMessageBox.information(self,"Error", "a is not comprime with 26")
            return
        result = ""
        if self.sender().text().lower() == "encrypt":
            result = affine.affine_encrypt(text, a, b)
        else:
            result = affine.affine_decrypt(text, a, b)
        self.affine_output.setPlainText(f"{result}")

    def hill_cipher_action(self):
        text = self.hill_input.toPlainText()
        str_matrix = self.hill_matrix.toPlainText()
        rows = str_matrix.strip().split("\n")
        key = np.array([list(map(int, row.split(','))) for row in rows])
        if self.sender().text().lower() == "encrypt":
            result = hill.hill_encrypt(text, key)
        else:
            result = hill.hill_decrypt(text, key)
        self.hill_output.setPlainText(f"{result}")

    def affine_hill_cipher_action(self):
        text = self.affine_hill_input.toPlainText()
        A_str_matrix = self.A_matrix.toPlainText()
        B_str_matrix = self.B_matrix.toPlainText()

        A_rows = A_str_matrix.strip().split("\n")
        A = np.array([list(map(int, row.split(','))) for row in A_rows])
        B_rows = B_str_matrix.strip().split("\n")
        B = np.array([list(map(int, row.split(','))) for row in B_rows])

        if self.sender().text().lower() == "encrypt":
            result = affine_hill.affine_hill_encrypt(text, A, B)
        else:
            result = affine_hill.affine_hill_decrypt(text, A, B)

        self.affine_hill_output.setPlainText(f"{result}")

