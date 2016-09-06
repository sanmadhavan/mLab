import hashlib
import os, random, struct
from Crypto.Cipher import AES
import xml.etree.ElementTree as ET
import base64
header="<file>\n"
footer="</file>\n"

import sys
sys.path.append('/opt/mchain/lib')

import mchainlog
logger = mchainlog.setup_custom_logger('root')
logger.debug('mchain util')




def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
	print out_filename
        out_filename ="/home/sanjeev/POC/DocRepo/encrypt/"+out_filename
	print out_filename

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = '/tmp/encryptedfile.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

    encrypteddata=file_get_contents(out_filename)
    return encrypteddata


def getChildTag (filepath,key):
	childheader="\t<datafile>\n"
	childfooter="\t</datafile>\n"
	filenameSTag="\t\t<filename>"
	filenameETag="</filename>\n"
	fileCksumSTag="\t\t<cksum>"
	fileCksumETag="</cksum>\n"
	fileDataSTag="\t\t<fdata>"
	fileDataETag="</fdata>\n"

	filename=os.path.basename(filepath)

	print "Filepath= "+filepath
	print "Filename ="+filename 
	cksum=getCkSum (filepath)

	print "File Cksum = "+str(cksum)

	encryptedData=encrypt_file(key, filepath, out_filename=None, chunksize=64*1024)

	fnameTag = filenameSTag
	fnameTag += filename
        fnameTag += filenameETag

	fcksumTag = fileCksumSTag
        fcksumTag += cksum
        fcksumTag += fileCksumETag

	dataTag = fileDataSTag
        dataTag += encryptedData
        dataTag += fileDataETag

	childXml = childheader
	childXml += fnameTag
        childXml += fcksumTag
	childXml += dataTag
	childXml += childfooter

	return childXml



def getCkSum(filepath):
        if os.path.exists (filepath) == False:
                return None
        md5 = hashlib.md5()
        f = open(filepath)
        for line in f:
                md5.update(line)
        f.close()

        return md5.hexdigest()

def file_get_contents(filename):
    with open(filename) as f:
        encoded = base64.b64encode(f.read())
        #return f.read()
        return encoded

