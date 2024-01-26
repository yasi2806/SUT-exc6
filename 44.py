listoutput = list()
class DatabaseDoctor:
   
   
    bimaran = {}
    barname = {}
    def add_patient(self, patient_id, name, family_name, age, height, weight):
        if patient_id not in self.bimaran.keys():   
            if int(age) < 0:
                output("error: invalid age")
            elif int(height) < 0:
                output("error: invalid height")
            elif int(weight) < 0:
                output("error: invalid weight")            
            else:
                self.bimaran[patient_id] = {
                    'name': name,
                    'family_name': family_name,
                    'age': age,
                    'height': height,
                    'weight': weight
                }
                output("patient added successfully")
        else:
            output("error: this ID already exists")

    
    
    def display_patient(self, patient_id):
        if patient_id in self.bimaran:
            patient_info = self.bimaran[patient_id]
            output(f"patient name: {patient_info['name']}")
            output(f"patient family name: {patient_info['family_name']}")
            output(f"patient age: {patient_info['age']}")
            output(f"patient height: {patient_info['height']}")
            output(f"patient weight: {patient_info['weight']}")
        else:
            output("error: invalid ID")

    def add_visit(self, patient_id, beginning_time):
        if patient_id in self.bimaran:
            if 9 <= int(beginning_time) <= 18:
                if beginning_time not in self.barname:
                    self.barname[beginning_time] = self.bimaran[patient_id]
                    output("visit added successfully!")
                else:
                    output("error: busy time")
            else:
                output("error: invalid time")
        else:
            output("error: invalid id")

    def delete_patient(self, patient_id):
        if patient_id in self.bimaran:
           
            for time in list(self.barname.keys()):
                if self.barname[time] == self.bimaran[patient_id]:
                    self.barname.pop(time)
            del self.bimaran[patient_id]
            output("patient deleted successfully!")
        else:
            output("error: invalid id")


    def display_visit_list(self,patient_id):
        output("SCHEDULE:")
       
        for time, patient_info in self.barname.items():
            output(f"{time}:00 {patient_info['name']} {patient_info['family_name']}")
def output(output):
        listoutput.append(output)
def result():
    for res in listoutput:
        print(res)
def main():
    doctor_db = DatabaseDoctor()

   
   
    while True:
        command = input()
        parts = command.split()

        if command == 'exit':
            result()
            break
        elif command == 'display visit list':
            doctor_db.display_visit_list(patient_id)

        elif len(parts) >= 3:
            action = parts[0]
            patient_id = parts[2]

            if action == 'add' and parts[1] == 'patient' and len(parts) == 8:
                doctor_db.add_patient(patient_id, parts[3], parts[4], parts[5], parts[6], parts[7])
            elif action == 'display' and parts[1] == 'patient':
                doctor_db.display_patient(patient_id)
            elif action == 'add' and parts[1] == 'visit' and len(parts)==4:   
                doctor_db.add_visit(patient_id, parts[3])
            elif action == 'delete' and parts[1] == 'patient':
                doctor_db.delete_patient(patient_id)
            else:
                output("invalid command")
        else:
            output("invalid command")


if __name__ == "__main__":
    main()