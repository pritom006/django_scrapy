from django.core.management.base import BaseCommand
from property_app.models import Property, Summary, PropertyRating
from ollama.ollama_service import interact_with_ollama

class Command(BaseCommand):
    help = "Rewrite property titles and descriptions, and generate summaries, ratings, and reviews using Ollama"

    def handle(self, *args, **kwargs):
        for property in Property.objects.all():
            # Rewrite title and description
            prompt = f"Rewrite this title: {property.title}"
            property.title = interact_with_ollama("llama3", prompt)

            description_prompt = f"Generate a description for this property: {property.title}"
            property.description = interact_with_ollama("llama3", description_prompt)
            property.save()

            # Generate summary
            summary_prompt = f"Summarize the following: {property.title} {property.description}"
            summary_text = interact_with_ollama("llama3", summary_prompt)
            Summary.objects.create(property=property, summary=summary_text)

            # Generate rating and review
            review_prompt = f"Generate a rating and review for this property: {property.title} {property.description}"
            review_text = interact_with_ollama("llama3", review_prompt)
            rating = float(review_text.split("Rating:")[1].split()[0])
            review = review_text.split("Review:")[1]
            PropertyRating.objects.create(property=property, rating=rating, review=review)

        self.stdout.write(self.style.SUCCESS("Properties processed successfully."))
