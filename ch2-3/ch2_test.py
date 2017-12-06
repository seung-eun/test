
#2-3. 변수 사용하기
print("문제 2-3")
seung_eun = "안녕하세요. 승은, 오늘은 파이썬을 좀 배워 볼까요?"
print(seung_eun)
print("\n")

#2-4. 대문자-소문자로 변환하기 : title(), upper(), lower() 메서드 사용
print("문제 2-4")
first_name = "Lee"
last_name = "seung eun"
full_name = first_name + " " + last_name
print("첫글자만 대문자로 : "+full_name.title())
print("전체 대문자로 : "+full_name.upper())
print("전체 소문자로 : "+full_name.lower())
print("\n")

#2-5. 탭, 줄바꿈 사용하기 : \t, \n 사용 (반드시 따옴표 안에 사용할 것)
print("문제 2-5")
print('\t알버트 아인슈타인은 이렇게 말했습니다.\n\t"결코 실수하지 않은 사람은 아무것도 시도하지 않은 사람이다."')
print("\n")

#2-6. 문자열 결합, 변수, 탭/줄바꿈 사용
print("문제 2-6")
famous_person = "알버트 아인슈타인"
message = '\n\t"결코 실수하지 않은 사람은 아무것도 시도하지 않은 사람이다."'
full_message = '\t'+famous_person+'은 이렇게 말했습니다.'+message
print(full_message)
print("\n")

#2-7. 공백 잘라내기 : strip()메서드 사용
print("문제 2-7")
person_name1 = " 이"
person_name2 = " 승은 "
print('\t'+"'"+person_name1+person_name2+"'")
print('\t'+"'"+person_name1.lstrip()+person_name2+"'")
print('\t'+"'"+person_name1.strip()+person_name2.strip()+"'")
print("\n")

print("문제 2-8")
print(2.0+6)
question2_8 = 4*2
print(question2_8)
print("\n")

print("문제 2-9")
favorite_number = 33
message = "my favorite number"+" is"+" "+str(favorite_number)
print("\n")

print("문제 2-10")

