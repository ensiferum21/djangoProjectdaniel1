#-------------------------------------------------

#https://github.com/Rayraegah/dhash

from PIL import Image
import os
from django.conf import settings



class dhash(object):
    """
    usage:
    calculate the dhash value of an image
    hash = dhash.calculate_hash(image)
    calculate the hamming distance between two images
    hamming_distance = dhash.hamming_distance(image1, image2)
    calculate the hamming distance between two dhash values
    hamming_distance = dhash.hamming_distance(dhash1, dhash2)
    """
    @staticmethod
    def calculate_hash(image):
        """
        calculate the dhash of an image
        :param image: PIL.Image
        :return: dhash (str)
        """
        difference = dhash.__difference(image)
        # 1 => 8, 8 => 16
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:
                # 0xf=>0x0f
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))
                decimal_value = 0
        return hash_string

    @staticmethod
    def hamming_distance(first, second):
        """
        calculate hamming distance
        :param first: dhash (str)
        :param second: dhash (str)
        :return: hamming distance
        """
        if isinstance(first, str):
            return dhash.hamming_distance_with_hash(first, second)

        hamming_distance = 0
        image1_difference = dhash.__difference(first)
        image2_difference = dhash.__difference(second)
        for index, img1_pix in enumerate(image1_difference):
            img2_pix = image2_difference[index]
            if img1_pix != img2_pix:
                hamming_distance += 1
        return hamming_distance

    @staticmethod
    def __difference(image):
        """
        find the difference with image
        :param image: PIL.Image
        :return: difference (int)
        """
        resize_width = 9
        resize_height = 8

        # resize enough to hide the details
        smaller_image = image.resize((resize_width, resize_height))


        # reduce color i.e. convert to grayscale
        grayscale_image = smaller_image.convert("L")

        # difference calculation
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(
                    pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    @staticmethod
    def hamming_distance_with_hash(dhash1, dhash2):
        """
        find difference using 2 dhash values
        :param dhash1: str
        :param dhash2: str
        :return: difference (int)
        """
        difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
        return bin(difference).count("1")
#------------------------------------------------
    def check_perceptual(image1):

        from django.core.files.storage import default_storage

        filename = "temporary_image.png"  # received file name
        tmp_file = os.path.join(settings.MEDIA_ROOT, 'tmp/'+filename)

        with default_storage.open('tmp/' + filename, 'wb+') as destination:
            for chunk in image1.chunks():
                destination.write(chunk)
        image1=Image.open(tmp_file)

        hash = dhash.calculate_hash(image1)

        image_directory_path=os.path.join(settings.MEDIA_ROOT,"images")
        for filename in os.listdir(image_directory_path):
            if os.path.isdir(image_directory_path+"\\"+filename): #skips the profile directory which was inside media/images folder
                continue
            #print(filename)
            image2 = Image.open(image_directory_path+"\\"+filename)
            hash2 = dhash.calculate_hash(image2)

            hamming_distance = dhash.hamming_distance_with_hash(hash, hash2)

            print("the hamming distance between images :", hamming_distance)

            if hamming_distance < 20:  # number set by me
                print("Similar Image")
                return False
            else:
                print("Different Image")



        return True
