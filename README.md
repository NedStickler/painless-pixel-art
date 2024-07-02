# Painless Pixel Art
Painless Pixel Art is a set of tools for creating simple pixel art objects.

## About
Generative AI has allowed for easy access to art generation for a variety of purposes. Asking generative AI to produce pixel art, however, results in a *stylised* output, and is not correctly represented with the appropriate number of pixels.

Painless Pixel Art addresses these issues by providing an interface to OpenAI's Dall-E 2 generative model that first generates requested imagery, and then removes the background and performs a simple downsampling operation.

The result is **true** pixel art.

## Getting started
To start using Painless Pixel Art follow the steps below.

### Prerequisites
Painless Pixel Art is implemented in Python 3.10+, which is the recommened usage version. To install Python 3.10+, visit [here](https://www.python.org/downloads/).

### Installation
To clone the repository and begin using Painless Pixel Art, follow these steps.
1. Clone the repository
```
git clone https://github.com/NedStickler/painless-pixel-art.git
```
2. Move into the repository
```
cd painless-pixel-art
```
3. Create a virtual environment in the repository
```
python -m venv venv
```
4. Activate the virtual environment. 
- On windows
```
.\venv\Scripts\activate
```
- On Unix or MaxOS
```
source venv/bin/activate
```
5. Install the package dependencies
```
pip install -r requirements.txt
```
6. Finally, generate an OpenAI API key to use for generating imagery. Guidance can be found [here](https://platform.openai.com/organization/api-keys).

## Usage
The following section covers an example use case and how the tool may be used.
