class Comment:
    def __init__(self, comment_by, date, time, content):
        self.comment_by = comment_by
        self.date = date
        self.time = time
        self.content = content

    def jsonify_comment(self):
        output_json = {}
        output_json["commentBy"] = self.comment_by
        output_json["date"] = self.date
        output_json["time"] = self.time
        output_json["commentContent"] = self.content
        return output_json

if __name__ == "__main__":
    test = Comment("me", "today", "now", "this is good");
    print test.jsonify_comment()
