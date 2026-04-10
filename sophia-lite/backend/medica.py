from datetime import datetime

class MedicaGeometrica:
    def __init__(self):
        self.logs = []

    def log_entry(self, mood, energy, sleep, stress, notes=""):
        self.logs.append({
            "time": str(datetime.now()),
            "mood": mood,
            "energy": energy,
            "sleep": sleep,
            "stress": stress,
            "notes": notes
        })
        return {"status": "logged"}

    def analyze(self):
        if not self.logs:
            return "No data yet."

        avg = lambda k: sum(e[k] for e in self.logs)/len(self.logs)

        insights = []
        if avg("sleep") < 6:
            insights.append("Low sleep → prioritize rest.")
        if avg("stress") > 7:
            insights.append("High stress → try grounding.")
        if avg("energy") < 4:
            insights.append("Low energy → hydrate, eat.")
        if avg("mood") < 4:
            insights.append("Low mood → reach out to someone.")

        return {
            "averages": {
                "mood": round(avg("mood"),2),
                "energy": round(avg("energy"),2),
                "sleep": round(avg("sleep"),2),
                "stress": round(avg("stress"),2)
            },
            "insights": insights or ["Stable patterns."],
            "note": "Not medical advice"
        }