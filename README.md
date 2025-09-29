# A3 to A4 Converter - Exam Script Processing Tool

A specialized Python application designed for academic institutions to efficiently convert A3-scanned exam scripts into individual A4 pages. This tool significantly reduces scanning time and administrative overhead when processing student exam booklets for storage and external moderation.

## Purpose

This application was developed to solve a common academic administrative challenge: efficiently processing double-page exam booklets for digital storage and moderation. Instead of scanning each page individually (which can take 3+ hours for just 20 scripts), this tool allows you to:

1. **Scan faster**: Scan entire A3 double-page spreads as single documents
2. **Process automatically**: Convert A3 scans into separate A4 pages with one click
3. **Save time**: Reduce scanning time by approximately 60%
4. **Streamline workflow**: Automate the tedious conversion process

## Key Features

- **Batch Processing**: Convert multiple A3 PDF files simultaneously
- **Smart Page Detection**: Automatically handles both landscape and portrait orientations
- **Flexible Page Order**: Choose whether left or right page appears first in output
- **GUI Interface**: User-friendly file browser for selecting scan directories
- **Output Organization**: Creates organized output folders with clear naming
- **Cross-Platform**: Works on Windows with Python 3.9+

## Technical Requirements

### Software Dependencies
- **Python**: 3.9 or higher
- **PowerShell**: 7.5+ (for automated setup)
- **Required Python Libraries**:
  - `pymupdf` - PDF manipulation and processing
  - `pypdf` - PDF reading and writing operations
  - `tkinter` - GUI file dialogs (usually included with Python)
  - `pathlib` - Modern path handling

### System Requirements
- **Operating System**: Windows 10/11
- **Memory**: 4GB+ RAM recommended for large PDF processing
- **Storage**: Sufficient space for input and output files
- **Display**: Standard desktop resolution for GUI dialogs

## Installation

### Automated Setup (Recommended)

1. **Download/Clone** the project to your local machine
2. **Open PowerShell** in the project directory
3. **Run the setup script**:
   ```powershell
   powershell.exe .\ps-base\macro.ps1
   ```

The automated setup will:
- Check for existing Python installation
- Install Python if needed (with admin privileges prompt)
- Install required Python packages
- Create the executable application
- Complete setup in 3-5 minutes

### Manual Setup

If you prefer manual installation:

```bash
# Install Python dependencies
pip install pymupdf pypdf

# Verify installation
python -c "import pymupdf, pypdf; print('Dependencies installed successfully')"
```

## Usage

### Quick Start

1. **Launch the application**:
   - After installation, find `converter-app.exe` in the project directory
   - Double-click to launch

2. **Select your scan folder**:
   - The application will prompt you to select a directory
   - Choose the folder containing your A3 PDF scans
   - Example: Desktop → "CIV2011F Scans"

3. **Choose page order**:
   - When prompted, specify which side appears first:
   - **"L" or "Left"**: Left page is the first page of the document
   - **"R" or "Right"**: Right page is the first page of the document

4. **Processing**:
   - The application processes at ~0.25 seconds per scan
   - Progress is shown in the console window
   - Output files are saved automatically

5. **Results**:
   - Converted A4 files are saved in a new subfolder
   - Example: "CIV2011F Scans - A4 Outputs"
   - Output folder opens automatically when complete

### Detailed Workflow

```
Input:  exam_script_01.pdf (A3 double-page scan)
        exam_script_02.pdf (A3 double-page scan)
        ...

Output: exam_script_01.pdf (A4 individual pages)
        exam_script_02.pdf (A4 individual pages)
        ...
        (in "Original Folder - A4 Outputs" directory)
```

### Example Usage Scenarios

**Scenario 1: Engineering Exam Scripts**
```
Input Folder:  "Desktop/CIV2011F Final Exam Scans"
Contents:      student_001.pdf, student_002.pdf, ...
Page Order:    Left page first (L)
Output:        "Desktop/CIV2011F Final Exam Scans - A4 Outputs/"
```

**Scenario 2: Mathematics Test Papers**
```
Input Folder:  "Documents/MAT101 Test 3 Scans"
Contents:      test_batch_1.pdf, test_batch_2.pdf, ...
Page Order:    Right page first (R)
Output:        "Documents/MAT101 Test 3 Scans - A4 Outputs/"
```

## Project Structure

```
a3toa4-converter/
├── src/
│   └── converter.py          # Main application logic
├── ps-base/
│   └── macro.ps1             # PowerShell setup script
├── converter-app.exe         # Built executable (created after setup)
├── README.md                 # This documentation
└── README.txt               # Original documentation
```

## How It Works

### Technical Process

1. **File Detection**: Scans directory for PDF files using glob patterns
2. **PDF Analysis**: Reads each A3 PDF and analyzes page dimensions
3. **Orientation Handling**: Detects landscape vs portrait orientation
4. **Page Splitting**: Mathematically divides A3 pages into left/right halves
5. **A4 Creation**: Creates new A4-sized pages with proper transformations
6. **Order Management**: Arranges pages according to user preference
7. **Output Generation**: Saves converted files with organized naming

### Mathematical Transformations

The application uses PyPDF's coordinate system to precisely split A3 pages:

- **A3 Landscape**: ~1191 × 842 points
- **A4 Portrait**: ~595 × 842 points
- **Split Point**: A3 width ÷ 2 = A4 width

```python
# Left half transformation
left_half.mediabox.lower_left = (0, 0)
left_half.mediabox.upper_right = (page_width / 2, page_height)

# Right half transformation  
right_half.mediabox.lower_left = (page_width / 2, 0)
right_half.mediabox.upper_right = (page_width, page_height)
right_half.add_transformation((1, 0, 0, 1, -page_width / 2, 0))
```

## Configuration Options

### Page Order Settings
- **Left First**: Use when the left page of the A3 scan is page 1 of the document
- **Right First**: Use when the right page of the A3 scan is page 1 of the document

### Output Settings
- **Automatic Naming**: Output folder uses input folder name + " - A4 Outputs"
- **Organized Structure**: Maintains original filenames for easy identification
- **Auto-Open**: Output folder opens in Windows Explorer when processing completes

## Troubleshooting

### Common Issues

**Issue**: Application won't start
- **Solution**: Ensure Python 3.9+ is installed and accessible from command line
- **Check**: Run `python --version` in PowerShell

**Issue**: PDF processing fails
- **Solution**: Verify input files are valid PDF documents
- **Check**: Try opening PDFs in a standard PDF viewer first

**Issue**: Output pages appear in wrong order
- **Solution**: Re-run and choose different page order (L vs R)
- **Tip**: Check the first page of your A3 scan to determine correct order

**Issue**: Missing dependencies
- **Solution**: Run the automated setup script again
- **Manual**: `pip install pymupdf pypdf`

### Performance Tips

- **Large Files**: For PDFs > 50MB, ensure sufficient RAM is available
- **Batch Size**: Process in smaller batches if memory issues occur
- **File Format**: Ensure input files are properly formatted PDFs

## Performance Metrics

- **Processing Speed**: ~0.25 seconds per A3 page
- **Time Savings**: Up to 60% reduction in scanning workflow
- **Efficiency**: 20 exam scripts processed in minutes instead of hours
- **Accuracy**: Maintains original scan quality and resolution

## Use Cases

### Academic Institutions
- **Exam Processing**: Convert exam booklet scans for digital storage
- **External Moderation**: Prepare files for external moderator review
- **Archive Management**: Organize historical exam records
- **Quality Assurance**: Standardize document formats across departments

### Administrative Workflows
- **Bulk Processing**: Handle large volumes of exam scripts efficiently
- **Standardization**: Ensure consistent A4 format for all processed documents
- **Time Management**: Free up staff time for more valuable activities
- **Digital Transformation**: Support paperless administrative processes

## Security & Privacy

- **Local Processing**: All conversions happen locally on your machine
- **No Cloud Upload**: Student data never leaves your computer
- **Original Preservation**: Original A3 scans remain unchanged
- **Secure Storage**: Output files maintain same security as input location

## License & Attribution

**Author**: Paul Namalomba  
**Created**: July 2025  
**Purpose**: Academic administrative efficiency  
**Institution**: University environment  

This tool is designed for educational institutions and administrative use. Please ensure compliance with your institution's data handling policies when processing student materials.

## Future Enhancements

Potential improvements for future versions:
- **Command-line interface** for automated workflows
- **Batch folder processing** for multiple directories
- **OCR integration** for searchable text extraction
- **Quality metrics** and processing statistics
- **Custom output naming** patterns
- **Progress bars** for large batch operations

## Support

For technical issues or questions:
1. Check the troubleshooting section above
2. Verify all requirements are met
3. Test with a small sample of files first
4. Ensure adequate system resources are available

**Note**: This tool is designed for academic administrative use and should be used in compliance with your institution's data handling and privacy policies.