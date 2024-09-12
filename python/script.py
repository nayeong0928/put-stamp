from PIL import Image
import sys

def make_transparent_except_color(input_image_path, output_image_path, color_range):
    """
    특정 색상 범위를 제외한 부분을 투명화하는 함수
    :param input_image_path: 입력 이미지 경로 (JPG/PNG)
    :param output_image_path: 출력 이미지 경로 (PNG)
    :param color_range: 허용할 색상 범위 (r_min, r_max, g_min, g_max, b_min, b_max)
    """
    img = Image.open(input_image_path).convert("RGBA")
    datas = img.getdata()
    
    r_min, r_max, g_min, g_max, b_min, b_max = color_range
    
    new_data = []
    for item in datas:
        r, g, b, a = item
        if r_min <= r <= r_max and g_min <= g <= g_max and b_min <= b <= b_max:
            new_data.append(item)  # 색상 범위에 포함되면 그대로 유지
        else:
            new_data.append((r, g, b, 0))  # 투명화

    img.putdata(new_data)
    img.save(output_image_path)

def overlay_png_on_jpg(jpg_image_path, png_image_path, output_image_path, position):
    jpg_image = Image.open(jpg_image_path)
    png_image = Image.open(png_image_path).convert("RGBA")

    jpg_image.paste(png_image, position, png_image)
    jpg_image.save(output_image_path)

def process_images(image1_path, image2_path, color_range, output_image_path, position):
    transparent_png_path = "transparent_image.png"

    make_transparent_except_color(image1_path, transparent_png_path, color_range)
    overlay_png_on_jpg(image2_path, transparent_png_path, output_image_path, position)

# 메인 실행 부분
if __name__ == "__main__":
    if len(sys.argv) < 10:
        print("Usage: python script.py <image1_path> <image2_path> <r_min> <r_max> <g_min> <g_max> <b_min> <b_max> <output_image_path> <x> <y>")
    else:
        image1_path = sys.argv[1]
        image2_path = sys.argv[2]
        r_min = int(sys.argv[3])
        r_max = int(sys.argv[4])
        g_min = int(sys.argv[5])
        g_max = int(sys.argv[6])
        b_min = int(sys.argv[7])
        b_max = int(sys.argv[8])
        output_image_path = sys.argv[9]
        x = int(sys.argv[10])
        y = int(sys.argv[11])
        
        color_range = (r_min, r_max, g_min, g_max, b_min, b_max)
        position = (x, y)

        process_images(image1_path, image2_path, color_range, output_image_path, position)
