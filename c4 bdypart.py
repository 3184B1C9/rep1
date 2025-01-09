class Human:
    def __init__(self):
        self.head = Head()
        self.body = Body()


class Head:
    component = "HEAD"  

    def __init__(self):
        self._parts = []  

    def get_parts(self):
        return self._parts

    def set_parts(self, part):
        self._parts.append(part)


class Body:
    component = "BODY"  

    def __init__(self):
        self._parts = []  

    def get_parts(self):
        return self._parts

    def set_parts(self, part):
        self._parts.append(part)


class BodyPart:
    def __init__(self):
        self._bpn = None  # Private variable
        self._num_of_bpn = None  # Private variable

    def get_bpn(self):
        return self._bpn

    def set_bpn(self, name):
        self._bpn = name

    def get_num_of_bpn(self):
        return self._num_of_bpn

    def set_num_of_bpn(self, num):
        self._num_of_bpn = num


# Create body parts
eye = BodyPart()
eye.set_bpn("eyes")
eye.set_num_of_bpn(2)

nose = BodyPart()
nose.set_bpn("nose")
nose.set_num_of_bpn(1)

legs = BodyPart()
legs.set_bpn("legs")
legs.set_num_of_bpn(2)

# Create an instance of Human
human = Human()

# Add body parts to the respective components
human.head.set_parts(eye)
human.head.set_parts(nose)
human.body.set_parts(legs)

# Print parts of the head
for part in human.head.get_parts():
    print(f"{Head.component} - {part.get_num_of_bpn()}{part.get_bpn()}")

# Print parts of the body
for part in human.body.get_parts():
    print(f"{Body.component} - {part.get_num_of_bpn()}{part.get_bpn()}")
