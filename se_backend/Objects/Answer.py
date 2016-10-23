from Comment import Comment

class Answer:
    def __init__(self, answer_by, date, time, answer_content):
        self.answer_by = answer_by
        self.date = date
        self.time = time
        self.content = answer_content
        self.comments = []

    def add_comment(self, comment_by, date, time, content):
        comment = Comment(comment_by, date, time, content)
        self.comments.append(comment)

    def add_comment_obj(self, comment_obj):
        self.comments.append(comment_obj);

    def jsonify_answer(self):
        output_json = {}
        output_json["answerContent"] = self.content
        output_json["answerBy"] = self.answer_by
        output_json["date"] = self.date
        output_json["time"] = self.time
        output_json["comments"] = []
        for comment in self.comments:
            output_json["comments"].append(comment.jsonify_comment())
        return output_json

if __name__ == "__main__":
    answer = Answer("me", "today", "now", "Yes")
    comment = Comment("him", "today", "5 minutes", "why yes")
    answer.add_comment("her", "yesterday", "9 mimutes", "why no")
    answer.add_comment_obj(comment)
    print answer.jsonify_answer()
