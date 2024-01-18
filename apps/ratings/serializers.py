from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    """
        Serializer allow complex data such as query set and model instances to convert to 
        native python data types.
        These data types can then be rendered to JSON, XML, etc.
    """

    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]
    
    def get_rater(self, obj):
        return obj.rater.username
    
    def get_agent(self, obj):
        return obj.agent.user.username
