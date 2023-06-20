from rest_framework import serializers
from .models import Movie, Actor, Review


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "reviews",
            "opening_date",
            "running_time",
            "overview",
            "actors",
        )
        read_only_fields = ["reviews"]


# -----------------------------------------------------------------------------------------
# 역관계를 사용할 경우 첫번째
# class MovieSerializer(serializers.ModelSerializer):
#     movie_reviews = serializers.PrimaryKeyRelatedField(
#         source="reviews", many=True, read_only=True
#     )

#     class Meta:
#         model = Movie
#         fields = (
#             "id",
#             "name",
#             "movie_reviews",
#             "opening_date",
#             "running_time",
#             "overview",
#         )

# -----------------------------------------------------------------------------------------
# 역관계를 사용할 경우 두번째
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = (
#             "id",
#             "name",
#             "reviews",
#             "opening_date",
#             "running_time",
#             "overview",
#         )
#         read_only_fields = ["reviews"]
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# serializers.Serializer 을 사용한 경우
# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField()
# opening_date = serializers.DateField()
# running_time = serializers.IntegerField()
# overview = serializers.CharField()

# def create(self, validated_data):
#     return Movie.objects.create(**validated_data) # ** : unpacking

# def update(self, instance, validated_data):
#     instance.name = validated_data.get("name", instance.name)
#     instance.opening_date = validated_data.get(
#         "opening_date", instance.opening_date
#     )
#     instance.running_time = validated_data.get(
#         "running_time", instance.running_time
#     )
#     instance.overview = validated_data.get("overview", instance.overview)
#     instance.save()
#     return instance
# -----------------------------------------------------------------------------------------


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = (
            "id",
            "name",
            "gender",
            "birth_date",
            "movies",
        )


# -----------------------------------------------------------------------------------------
# serializers.Serializer을 사용한 경우
# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField()
# gender = serializers.CharField()
# birth_date = serializers.DateField()

# def create(self, validated_data):
#     return Actor.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.name = validated_data.get("name", instance.name)
#     instance.gender = validated_data.get("gender", instance.gender)
#     instance.birth_date = validated_data.get("birth_date", instance.birth_date)
#     instance.save()
#     return instance
# -----------------------------------------------------------------------------------------


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = (
            "id",
            "movie",
            "username",
            "star",
            "comment",
            "created",
        )
        # extra_kwargs = {
        #     "movie": {"read_only": True},
        # }
