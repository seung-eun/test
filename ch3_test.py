#3-1. 메세지 단순히 출력해보기
print("문제 3-1")
animals = ['강아지', '고양이', '원숭이', '병아리', '곰', '펭귄']
print(animals[0])
print(animals[1])
print(animals[-1])
print("\n")

#3-2. 리스트 + 문자열 함께 출력하기
print("문제 3-2")
message1 = animals[0] + "는 " + "멍멍"
message2 = animals[1] + "는 " + "야옹야옹"
message3 = animals[3] + "는 " + "삐약삐약"
print(message1+"\n"+message2+"\n"+message3)
print("\n")

#3-4. 리스트 + 문자열 함께 출력하기
print("문제 3-4")
invite_dinner = ['승은', '상원', '서로', '지정']
message1 = invite_dinner[0] + "아, 다음주에 저녁 먹자"
message2 = invite_dinner[1] + "아, 다음주에 저녁 먹자"
message3 = invite_dinner[2] + "야, 다음주에 저녁 먹자"
message4 = invite_dinner[-1] + "아, 다음주에 저녁 먹자"
print(message1+"\n"+message2+"\n"+message3+"\n"+message4)
print("\n")

#3-5. 리스트에서 제거할 항목 꺼내기 :
# 리스트 이름.pop(인덱스, 값) / del 리스트 이름[인덱스] / 리스트 이름.remove(값)
print("문제 3-5")
cannot_come = invite_dinner.pop(-2)
print("다음주에"+" "+cannot_come+"가 못 온다고 했다.")
print("\n")

#3-6. 리스트에 인원 추가하기 : 리스트 이름.insert(인덱스, 값) / 리스트 이름.append(값)
print("문제 3-6")
message3_6 = invite_dinner[0]+", "+invite_dinner[1]+", "+invite_dinner[2]+"에게.\n몇명 더 초대할게!"
print(message3_6)
invite_dinner.insert(0, "현종")
invite_dinner.insert(3, "한결")
invite_dinner.append("수지")
message1 = invite_dinner[0] + "아, 다음주에 저녁 먹자"
message2 = invite_dinner[1] + "아, 다음주에 저녁 먹자"
message3 = invite_dinner[2] + "아, 다음주에 저녁 먹자"
message4 = invite_dinner[-3] + "아, 다음주에 저녁 먹자"
message5 = invite_dinner[-2] + "아, 다음주에 저녁 먹자"
message6 = invite_dinner[-1] + "야, 다음주에 저녁 먹자"
print(message1+"\n"+message2+"\n"+message3+"\n"+message4+"\n"+message5+"\n"+message6)
print("\n")

#3-7. 리스트에서 제거할 항목 꺼내기 :
print("문제 3-7")
message3_7 = invite_dinner[0]+", "+invite_dinner[1]+", "+invite_dinner[2]+", "+invite_dinner[-3]+", "+invite_dinner[-2]+", "+invite_dinner[-1]+"에게.\n식당에 자리가 없대ㅠ"
print(message3_7)
cannot_invite = invite_dinner.pop()
print(cannot_invite+"에게.\n식당에 예약이 안돼서, 날짜를 다시 잡으려고 해. 미안해!")
cannot_invite = invite_dinner.pop()
print(cannot_invite+"에게.\n식당에 예약이 안돼서, 날짜를 다시 잡으려고 해. 미안해!")
cannot_invite = invite_dinner.pop()
print(cannot_invite+"에게.\n식당에 예약이 안돼서, 날짜를 다시 잡으려고 해. 미안해!")
cannot_invite = invite_dinner.pop()
print(cannot_invite+"에게.\n식당에 예약이 안돼서, 날짜를 다시 잡으려고 해. 미안해!")
message3_7_1 = invite_dinner[0]+", "+invite_dinner[1]+"에게,\n 둘하고는 예정대로 보려고 하는데 괜찮을까?"
print(message3_7_1)
del invite_dinner[1]
del invite_dinner[0]
print(invite_dinner)
print("\n")

#3-8. 리스트 정렬하기 : 
# 알파벳순서로 정렬 - sort(), sort(reverse=True), sorted(), 역순으로 정렬 - reverse()
print("문제 3-8")
want_go = ['peru', 'palau', 'kyoto', 'sapporo', 'lijiang', 'fiji']
print("sorted 함수 써보기")
print(want_go)
print(sorted(want_go))
print(want_go)
print("reverse 함수 써보기")
want_go.reverse()
print(want_go)
want_go.reverse()
print(want_go)
print("sort 함수 써보기")
want_go.sort()
print(want_go)
want_go.sort(reverse=True)
print(want_go)

#3-9. 리스트 길이 구하기 : 길이(항목) 구하기 - len()
print("문제 3-9")
invite_dinner = ['승은', '상원', '서로', '지정']
print(invite_dinner)
print(len(invite_dinner))

#3-10. 리스트 관련 함수 다 써보기
print("문제 3-10")
my_favorite = ["늦잠자기", "카페가서 책보기", "교외나들이", "숯불닭갈비에 맥주"]
message = "Q. 빨간날에 뭐할거야?"
print(message)
print("A. 이렇게 할거야.\n")
print(my_favorite)
message = "Q. 더 하고싶은 건 없어?"
print(message)
my_favorite.insert(-1, "목도리 사기")
print("A. 추가해보자면\n" + str(my_favorite))
message = "Q. 또 더 없어?"
print(message)
my_favorite.append("한강가서 산책으로 마무리")
print("A. 그럼 마무리로 이렇게\n" + str(my_favorite))
message = "Q. 생각해보니 좀 많은 것 같은데?"
print(message)
not_to_do = my_favorite.pop(0)
print("A. 그러면 " + not_to_do +" 빼고 일찍 일어날래. 이렇게만 해야지\n" + str(my_favorite))
message = "Q. 또 더 뺄 거 없어?"
print(message)
del my_favorite[0]
print("A. 그러면 이렇게만..\n" + str(my_favorite))
message = "Q. 그럼 난 언제쯤 합류할까?"
print(message)
my_favorite.reverse()
print("A. 거꾸로 생각하면 일정이 이렇거든\n" + str(my_favorite) + "\n 맥주마실 때쯤?")



