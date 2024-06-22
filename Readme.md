# Markdown to Slides Previewer

This project is a Streamlit app that allows users to input Markdown text and generate a live preview of slides on the right side of the screen. It uses Marp CLI to convert Markdown to HTML slides.

## Features

- **Markdown Input**: Users can input Markdown text to create slides.
- **Live Preview**: A live preview of the slides is displayed on the right side.
- **Interactive**: The app provides an interactive way to see changes in real-time as you edit your Markdown.

## Installation

### Prerequisites

- **Python**: Make sure Python is installed on your system.
- **Node.js**: Marp CLI requires Node.js. You can download it from [nodejs.org](https://nodejs.org/).

### Steps

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/your-username/markdown-to-slides-previewer.git
   cd markdown-to-slides-previewer
   ```

2. **Install Python Dependencies**:

   ```sh
   pip install streamlit
   ```

3. **Install Marp CLI**:
   ```sh
   npm install -g @marp-team/marp-cli
   ```

## Usage

1. **Run the Streamlit App**:

   ```sh
   streamlit run app.py
   ```

2. **Open Your Browser**:

   - Go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. **Enter Markdown**:
   - Enter your Markdown text in the input area on the left side.
   - Click the "Generate Preview" button to see the slides on the right side.

## Example

Here’s an example of Markdown that you can use in the app:

```markdown
# Slide 1

Welcome to my presentation!

---

# Slide 2

Here is some more content.

---

# Slide 3

- Point 1
- Point 2
- Point 3
```

## Project Structure

```
markdown-to-slides-previewer/
├── app.py          # Main Streamlit app script
├── slides.md       # Temporary file for Markdown input (auto-generated)
├── slides.html     # Temporary file for HTML slides (auto-generated)
└── README.md       # Project README file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
