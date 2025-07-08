import coin_count
import coin_identification
import cv2
import os
import crop_coin_and_update

output_dir = '/Users/USER/Pictures/project/coins/coins'


sum =0.0


def photo_to_number(photo):
    photo = photo.lower()

    if photo.startswith("10 agr"):
        return 0.1
    if photo.startswith("1 shekel"):
        return 1
    if photo.startswith("2 shekel"):
        return 2
    if photo.startswith("5 shekel"):
          return 5
    if photo.startswith("10 shekel"):
        return 10
    if photo.startswith("half") :
        return 0.5

    if photo.startswith("the coin was not found."):
        return 0







    #cv2.imshow('test2', new_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()




def calculate_sum(image_path):
    total_sum = 0.0
    number_of_coins = coin_count.coin_num(image_path)
    print(number_of_coins)

    coin, coins_img = coin_identification.identification(image_path)
    #print(coin)
    coin_value = photo_to_number(coin)
    total_sum += coin_value
    #print(total_sum)

    output_path = os.path.join(output_dir, f'coin_{1}.png')
    cv2.imwrite(output_path, coins_img)


    for i in range(1, number_of_coins):
       coin, coins_img = coin_identification.identification(output_path)
       coin_value = photo_to_number(coin)



       if coin_value is not None:
         total_sum += coin_value
         #print(total_sum)
       else:
         print(f"Warning: photo_to_number returned None for coin: {coin}")

       output_path = os.path.join(output_dir, f'coin_{i + 1}.png')
       cv2.imwrite(output_path, coins_img)
    # print("coin %d " % (i + 1), coin)

    # cv2.imshow('test2', new_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return total_sum


#print(sum('/Users/USER/Pictures/Screenshots/Screenshot (305).png'))
#print(calculate_sum('/Users/USER/Pictures/project/coins/all_coins/coin_3.png'))

def sum_money():
    return sum


