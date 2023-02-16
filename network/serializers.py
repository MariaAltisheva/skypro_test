from rest_framework import serializers

from .models import Item, Link

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    def validate(self, data):
        instance = self.instance
        if instance:
            current_debt = instance.debt
            new_debt = data.get('debt')
            if new_debt and (new_debt != current_debt):
                data.update({'debt': current_debt}) # в данном случае мы не позволяем через API менять задолженность
        return data
    items = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Link
        fields = '__all__'

