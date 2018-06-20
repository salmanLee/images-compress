# images-compress
    JPG and PNG compression script
# OS
    linux/macOS/windows. I had no test ohters. You can try and tell me.
# python
    you need to install Python3
# pngquant
    you need to install pngquant for .png
    build:
    npm install pngquant
# guetzli
    you need to install quetzli for .jpg
    build:
    https://github.com/google/guetzli/edit/master/README.md

# how to use
    $ python ic.py /home/xx/xx
# parameters
    required parameter: inputPath
    optional parameter: outputPath ( If you don't write output path, or output path is the same as input path, the output images overrides the original images )
    optional parameter: imgType ( only support jpg or png )
