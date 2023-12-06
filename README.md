# URLShortener

This is a URLShortener Site made by Django. Algorothm made in this site is very efficient.

Absolutely! Here's a revised README file with a focus on the URL shortener functionality in your Django project:

---

This Django-based web application allows users to shorten URLs and optionally encrypt and decrypt the stored links using a user-provided key. It provides functionality to generate short links for sharing and, if enabled, secure encryption and decryption of the stored URLs.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage

### Shorten URL

- Access the application in your browser.
- Navigate to the URL shortening page.
- Paste the desired YouTube video link.
- Click the "Shorten" button to generate a short link for sharing.

### Encryption and Decryption (Optional)

- Access the encryption/decryption page (if enabled).
- Enter the short link and encryption key to encrypt the link.
- Enter the encrypted link and decryption key to decrypt the link.

## URL Routes

- `/shorten-url/`: Endpoint for shortening a URL.
- `/encrypt-decrypt/`: Endpoint for encryption and decryption (if enabled).

## Additional Notes

- Ensure proper handling and storage of encryption keys.
- Customize encryption and decryption logic as needed.
- Implement secure practices for handling user-provided keys.
- Customize the `Url` model or encryption/decryption methods according to requirements.

## Screen Shots
![image](https://github.com/nisheshjain12/Url-Shortner/assets/89805538/c89e65fd-f6e5-4b37-b328-68326483dcc8)
![image](https://github.com/nisheshjain12/Url-Shortner/assets/89805538/516462e7-b4a0-42cf-8014-ea56ff45d7c0)

## License

This project is licensed under the [MIT License](LICENSE).

---
