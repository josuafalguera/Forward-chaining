facts = [
    "the patient has fatigue",
    "the patient has anaemia"
]
rules = [
    "if the patient has cancer, then the patient has loss of appetite",
    "if the patient has fatigue and the patient has anaemia, then the patient has scurvy",
    "if the patient has headache and the patient has a very high fever and the patient has a low platelet, then the patient has dengue fever",
    "if the patient is feeling tired and the patient is very thirsty and the patient experience weight loss, then the patient has type one diabetes",
    "if the patient is feeling tired and the patient is feeling weak, then the patient has fatigue",       
    "if the patient has fatigue and the patient has headache and the patient has loss of appetite and the patient has pale skin color, then the patient has anaemia",
    "if the patient has cancer, then the patient is feeling weak",
    "if the patient experience weight loss and the patient has pale skin color, then the patient has cancer"
]

def enter_fact(input):
    facts.append(input)

def enter_rule(input):
    rules.append(input)

def generate_new_facts():
    new_fact_added = True
    while new_fact_added:
        new_fact_added = False
        for rule in rules:
            parts = rule.split(", then ")
            conditions = parts[0][3:].split(" and ") # remove "if " from conditions
            conditions_met = all(condition in facts for condition in conditions)
            if conditions_met:
                new_fact = parts[1]
                if new_fact not in facts:
                    facts.append(new_fact)
                    new_fact_added = True

def show_current_facts_and_rules():
    print("Facts: ")
    for i, fact in enumerate(facts, start=1):
        print(f"{i}. {fact}")

    print("\nRules: ")
    for i, rule in enumerate(rules, start=1):
        print(f"{i}. {rule}")

def delete_facts():
    facts.clear()

def delete_rules():
    rules.clear()

def main():
    choice = 0
    while choice != 6:
        print("---------------------------------------")
        print("***Knowledge Base***")
        show_current_facts_and_rules()
        print("---------------------------------------")

        print("[1] Enter a fact")
        print("[2] Enter a rule")
        print("[3] Generate new facts")
        print("[4] Delete current fact/s")
        print("[5] Delete current rule/s")
        print("[6] Exit")
        choice = int(input("Enter what you want to do: "))
        print("\n")

        if choice == 1:
            new_fact = input("New Fact: ")
            enter_fact(new_fact)
        elif choice == 2:
            new_rule = input("New Rule: ")
            enter_rule(new_rule)
        elif choice == 3:
            generate_new_facts()
        elif choice == 4:
            delete_facts()
        elif choice == 5:
            delete_rules()

if __name__ == "__main__":
    main()
