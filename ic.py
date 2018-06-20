import os
import argparse

# required parameter: inputPath
# optional parameter: outputPath ( If you don't write output path, or output path is the same as input path, the output images overrides the original images )
# optional parameter: imgType ( only support jpg or png )
# author: Salman Lee
# date: 2018.05.28
 
# global
IMGSLIST = []
JPG = 'jpg'
JPG2 = 'JPG'
JPG3 = 'jpeg'
JPG4 = 'JPEG'
PNG = 'png'
PNG2 = 'PNG'
OVERWRITE = False

# foreach all files in filepath
def getImgs(filepath , imgType):
    typeFlag = False
    try:
        files = os.listdir(filepath)
    except Exception:
        print('cannot find the input path')
        return []
    else:
        for file in files:
            file_dir = os.path.join(filepath,file)
            if os.path.isdir(file_dir):
                getImgs(file_dir , imgType)
            else:
                if imgType == JPG:
                    typeFlag = file.endswith(JPG) or file.endswith(JPG2) or file.endswith(JPG3) or file.endswith(JPG4)
                elif imgType == PNG:
                    typeFlag = file.endswith(PNG) or file.endswith(PNG2)
                if typeFlag :
                    obj = dict(imgPath=os.path.join(filepath,file_dir), imgName=file)
                    IMGSLIST.append(obj)
        return IMGSLIST

#compressing
def imgCompress( inputP, outputP ,imgType ):
    if imgType == JPG:
        try:
            os.system('guetzli'+' '+inputP+' '+outputP)
        except Exception:
            print('compressing jpg error , error for the programmer ')
    elif imgType == PNG:
        try: 
            os.system('pngquant'+' '+'--force'+' '+'--output'+' '+outputP+' '+inputP)
        except Exception:
            print('compressing png error , error for the programmer ')

#run script
def running( inputPath , outputPath ,imgType , overwrite):
    imgsArr = []
    if os.path.exists(inputPath) == False:
        print('cannot find input path')
        return
    elif outputPath == None:
        overwrite = True
        outputPath = inputPath
    elif inputPath == outputPath:
        overwrite = True
    elif os.path.exists(outputPath) == False:
        print('cannot find output path')
        return
    if imgType == JPG or imgType == JPG2 or imgType == JPG3 or imgType == JPG4 :
        imgType = JPG
    elif imgType == PNG or imgType == PNG2:
        imgType = PNG
    else:
        print('imgType only can input jpg or png')
    #get func
    imgsArr = getImgs( inputPath , imgType )
    if len(imgsArr) < 1:
        print('cannot find image with '+imgType)
        return
    elif len(imgsArr) >= 1:
        temp = 0
        out = ''
        for obj in imgsArr:
            if overwrite == True:
                out = obj['imgPath']
            else:
                out = outputPath + '/' + obj['imgName']
            print('Compressing...')
            print('input:',obj['imgPath'])
            print('output:',out)
            #get func
            imgCompress( obj['imgPath'] , out , imgType )
            temp += 1
            if temp == len(imgsArr):
                print('All done!! '+'('+str(temp)+'/'+str(len(imgsArr))+')')
            else:
                print('('+str(temp)+'/'+str(len(imgsArr))+') is done!')

# index
parser = argparse.ArgumentParser(description=
'JPG & PNG compression script.'+'\n# required parameter: inputPath;'+
'\n# optional parameter: outputPath ( If you donnot write output path, or output path is the same as input path, the output images overrides the original images );'+
'\n# optional parameter: imgType ( only support jpg or png ).')
parser.add_argument('-type','--imgType',const=JPG,default=JPG , nargs='?',
                   help='JPG or PNG')
parser.add_argument('input',   nargs=1,
                   help='images origin folder')
parser.add_argument('-out','--output',nargs='?',
                   help='images target folder')
args = parser.parse_args()
running( args.input[0] , args.output, args.imgType ,OVERWRITE)
