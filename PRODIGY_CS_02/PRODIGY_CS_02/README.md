#Task 2
<b>Image Encryption Tool</b>

This Python program implements a simple image encryption tool using pixel manipulation techniques. The program can encrypt and decrypt images by performing basic mathematical operations on the pixel values. It is designed to be user-friendly, guiding users through the encryption and decryption processes with clear prompts.

<b>Features</b>

- <b>Image Encryption:</b> Users can encrypt an image by applying a mathematical operation to each pixel value, effectively altering the image.
- <b>Image Decryption:</b> The program can reverse the encryption process to restore the original image.
- <b>User Input:</b> Users can specify the image file and the encryption key.
- <b>File Handling:</b> The program saves the encrypted and decrypted images to specified file paths.

<b>How It Works</b>

1. <b>Encrypt Image:</b> Multiplies each pixel value by a key and then divides by the key plus one to create the encrypted image.
2. <b>Decrypt Image:</b> Reverses the encryption process by multiplying each pixel value by the key plus one and then dividing by the key.

<b>Usage</b>
<ol>
<li><b>Run the Program:</b> Execute the script to start the Image Encryption program.</li>
<li><b>Select Action:</b> Choose 'e' for encryption, 'd' for decryption, or 'q' to quit.</li>
<li><b>Encrypt Image:</b></li>
  <ul>
    <li>Enter the encryption key.</li>
    <li>Specify the location or URL of the image to be encrypted.</li>
  </ul>
<li><b>Decrypt Image:</b></li>
  <ul>
    <li>Enter the decryption key.</li>
    <li>Specify the location of the encrypted image.</li>
  </ul>
<li><b>View Results:</b> The program saves and indicates the location of the encrypted and decrypted images.</li>
</ol>

This code was developed as part of my internship at The Prodigy Infotech, showcasing a basic approach to image encryption and decryption through pixel manipulation.
