import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from pathlib import Path

# Add the parent directory to path so we can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the init function from zor/main.py
from zor.main import init

class TestInitFunction(unittest.TestCase):

    @patch('zor.main.api_key_valid', True) 
    @patch('zor.main.generate_with_context')
    @patch('zor.main.typer.confirm')
    @patch('zor.main.typer.prompt')
    @patch('zor.main.Console')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.iterdir')
    def test_basic_project_creation(self, mock_iterdir, mock_mkdir, mock_exists, 
                                   mock_console, mock_prompt, mock_confirm, mock_generate):
        # Setup mocks
        mock_exists.return_value = False
        mock_iterdir.return_value = []
        mock_confirm.return_value = True
        mock_prompt.return_value = "test_project"
        mock_console_instance = MagicMock()
        mock_console.return_value = mock_console_instance
        mock_console_instance.status.return_value.__enter__.return_value = MagicMock()
        
        # Mock AI responses
        mock_generate.side_effect = [
            # First call - project plan
            """PROJECT_TYPE: Python CLI Tool
            MAIN_TECHNOLOGIES: Python, Typer
            ARCHITECTURE: Simple CLI
            SCAFFOLD_COMMAND: NONE
            SCAFFOLD_TYPE: NONE""",
            
            # Second call - file content
            """FILE: main.py
```
import typer
app = typer.Typer()

@app.command()
def hello():
    print("Hello World")

if __name__ == "__main__":
    app()
```"""
        ]
        
        # Execute the function with test parameters
        with patch('builtins.open', unittest.mock.mock_open()):
            init(prompt="create a simple python cli", install=False, run=False)
        
        # Verify expected interactions
        mock_exists.assert_called()
        
        # Updated assertion to expect mkdir to be called twice
        self.assertEqual(mock_mkdir.call_count, 2)
        
        # Verify the arguments passed to mkdir
        mock_mkdir.assert_any_call(exist_ok=True, parents=True)  # First call
        mock_mkdir.assert_any_call(parents=True, exist_ok=True)  # Second call
        
        # Check that generate_with_context was called twice
        self.assertEqual(mock_generate.call_count, 2)

if __name__ == '__main__':
    unittest.main()
