good_words_list = []
bad_words_list = []
# 내부적으로만 관리되는 금지어 목록
forbidden_words = ['정원재', '원재']

def word_learning_system():
    print("📋 단어 분류 및 저장 프로그램 📋")
    # 금지어 출력 부분을 삭제했습니다.
    print("(종료: '그만', 목록 확인: '목록', 삭제: '삭제')\n")

    while True:
        user_input = input("단어 입력: ").strip()

        if not user_input: continue
        if user_input == '그만': break

        # 목록 확인
        if user_input == '목록':
            print(f"\n✨ 좋은 단어: {good_words_list}")
            print(f"⚠️ 나쁜 단어: {bad_words_list}\n")
            continue

        # 단어 삭제
        if user_input == '삭제':
            target = input("삭제할 단어를 입력하세요: ").strip()
            if target in good_words_list:
                good_words_list.remove(target)
                print(f"🗑️ '{target}'이(가) 좋은 단어장에서 삭제되었습니다.")
            elif target in bad_words_list:
                bad_words_list.remove(target)
                print(f"🗑️ '{target}'이(가) 나쁜 단어장에서 삭제되었습니다.")
            else:
                print(f"🔍 '{target}'은(는) 목록에 존재하지 않습니다.")
            print("-" * 30)
            continue

        # 금지어 체크 (화면엔 안 나오지만 입력 시 차단)
        if any(f_word in user_input for f_word in forbidden_words):
            print("❌ 사용할 수 없는 단어가 포함되어 있습니다.")
            print("-" * 30)
            continue

        # 1단계: 이미 저장된 단어인지 확인
        if user_input in good_words_list:
            print(f"📢 '{user_input}'은(는) '좋은 단어입니다.'")
            continue
        if user_input in bad_words_list:
            print(f"📢 '{user_input}'은(는) '나쁜 단어입니다.'")
            continue

        # 2단계: 새 단어 분류
        print(f"'{user_input}'은(는) 처음 보는 단어네요! 어떤 성격인가요?")
        choice = input("1.좋은 단어  2.나쁜 단어 (숫자 입력): ")

        if choice == '1':
            good_words_list.append(user_input)
            print(f"✅ '{user_input}'이(가) 좋은 단어장에 추가되었습니다.")
        elif choice == '2':
            bad_words_list.append(user_input)
            print(f"❌ '{user_input}'이(가) 나쁜 단어장에 추가되었습니다.")
        else:
            print("⚠️ 입력이 잘못되었습니다. 저장되지 않았습니다.")

        print("-" * 30)

word_learning_system()
