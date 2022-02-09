import urllib.request

# 다운로드 할 이미지 경로
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
# 저장할 파일 경로 및 이름
imgName = "C:/Users/sonhyeonjin/Desktop/대외활동/K-Trainig/깃허브/google.png"
# 파일 다운로드
# urlretrieve(URL, 저장할 파일 경로_
urllib.request.urlretrieve(url,imgName)
print("저장완료")
