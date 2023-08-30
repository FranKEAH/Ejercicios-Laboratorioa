persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True,
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

if 'skills' in persona:
    skills_list = persona['skills']
    num_skills = len(skills_list)
    
    if num_skills % 2 == 1:
        middle_skill_index = num_skills // 2
        middle_skill = skills_list[middle_skill_index]
        print("Habilidad del medio:", middle_skill)
    else:
        second_middle_skill_index = num_skills // 2
        first_middle_skill_index = second_middle_skill_index - 1
        first_middle_skill = skills_list[first_middle_skill_index]
        second_middle_skill = skills_list[second_middle_skill_index]
        print("Habilidades del medio:", first_middle_skill, "y", second_middle_skill)
else:
    print("El diccionario no contiene la clave 'skills'.")
if 'skills' in persona:
    skills_list = persona['skills']
    
    if 'Python' in skills_list:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")
else:
    print("El diccionario no contiene la clave 'skills'.")
if 'skills' in persona:
    skills_list = persona['skills']
    
    if 'JavaScript' in skills_list and 'React' in skills_list:
        print("Él es un desarrollador frontend.")
    elif 'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
        print("Él es un desarrollador backend.")
    elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
        print("Él es un desarrollador fullstack.")
    else:
        print("Título desconocido.")
else:
    print("El diccionario no contiene la clave 'skills'.")
