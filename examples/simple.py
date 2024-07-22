from code_video import CodeScene


# Here we define the class that will be used to create the video
class MyScene(CodeScene):
    # The constructor is the method that is called when the class is created
    def construct(self):
        # This does the actual code display and animation
        self.animate_code_comments("examples/simple.py")

        # and finally we wait 5 seconds before finishing
        self.wait(5)
