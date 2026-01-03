def save(message):
    with open("chat.txt", "a") as file:
        file.write(message + "\n")

def chatbot():
    print("hello! sir how can help you")
    save("chat started")

    while True:
        print("\nchoose the section:")
        print("1.admission related questions")
        print("2.college information")
        print("3.academics")
        print("4.placements")
        
        section = input("enter the section number: ").lower()
        
        if section == "exit":
            answer = "thank you. have a nice day"
            print("chatbot:", answer)
            save("chatbot:" + answer)
            break
            
        user = input("ask your questions: ").lower()
        save("user:" + user)
        
        # Section 1: Admission
        if section == "1":
            if "document" in user:
                answer = """Class 10 Mark Sheet & Passing Certificate, Class 12 Mark Sheet & Passing Certificate, Transfer Certificate (TC), Migration Certificate, Character Certificate, Caste/Category Certificate, Domicile Certificate, CET Scorecard, Passport-size Photographs, Government-issued ID Proof, Medical Certificate"""
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "fees" in user:
                answer = "OPEN : 84k , OBC : 45K , SEBC/EWS : 11K , SC/ST : 5K"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "hostel" in user:
                answer = "hostel facility are available"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            else:
                answer = "For more information call in college or visit in office"
                print("chatbot:", answer)
                save("chatbot:" + answer)

        # Section 2: College Information
        elif section == "2":
            if "established" in user:
                answer = "Matoshri college was established in 2008 and it is affiliated to savitribai phule university. It is autonomous and AICTE approved"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "date and time" in user:
                answer = "The college start on 15 september 2025 and time was 08.00 am to 03.00 pm"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "facility" in user:
                answer = "library, computer labs, gym, sports facilities and ground"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            else:
                answer = "for more information visit in college or call in office"
                print("chatbot:", answer)
                save("chatbot:" + answer)

        # Section 3: Academics
        elif section == "3":
            if "courses" in user:
                answer = "Bachelor of technology = Computer Engineering, IT engineering, AI and Data science engineering, mechanical engineering, civil engineering"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "syllabus" in user:
                answer = "courses syllabus details in syllabus section in this website"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "faculty" in user:
                answer = "faculty details in courses section respectively"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            else:
                answer = "for more information visit the college or call in office"
                print("chatbot:", answer)
                save("chatbot:" + answer)

        # Section 4: Placements
        elif section == "4":
            if "rate" in user:
                answer = "Placement rate was 90%"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "internship" in user:
                answer = "The internship details are in placements section in website"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            elif "companies" in user:
                answer = "TCS, Infosys, Tech Mahindra, HCL, etc"
                print("chatbot:", answer)
                save("chatbot:" + answer)
            else:
                answer = "for more information call in office or visit placement officer"
                print("chatbot:", answer)
                save("chatbot:" + answer)
        
        else:
            answer = "Invalid section. please choose number 1 to 4"
            print("chatbot:", answer)
            save("chatbot:" + answer)

# Start the chatbot
chatbot()
