from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.last()
    data = BannerSerializer(banner).data
    return Response(data)


@api_view(['GET'])
def get_all(request):
    offer = Offer.objects.order_by("-id")[:6]
    data = OfferSerializer(offer, many=True).data
    return Response(data)


@api_view(['GET'])
def get_option(request):
    option = PaymentOption.objects.order_by("-id")[:3]
    data = PaymentOptionSerializer(option, many=True).data
    return Response(data)


@api_view(['GET'])
def get_all_offer(request):
    offer = Offer.objects.all()
    data = OfferSerializer(offer, many=True).data
    return Response(data)


@api_view(['GET'])
def get_special(request):
    offer = SpecialOffer.objects.last()
    data = SpecialOfferSerializer(offer).data
    return Response(data)


@api_view(['GET'])
def get_builder(request):
    builder = Builder.objects.order_by("-id")[:4]
    data = BuilderSerializer(builder, many=True).data
    return Response(data)


@api_view(['GET'])
def get_single(request, pk):
    offer = Offer.objects.get(id=pk)
    data = OfferSerializer(offer).data
    return Response(data)


@api_view(['GET'])
def get_about(request):
    content = AboutUs.objects.last()
    data = AboutUsSerializer(content).data
    return Response(data)


@api_view(['GET'])
def get_service(request):
    service = Service.objects.order_by("-id")[:4]
    data = ServiceSerializer(service, many=True).data
    return Response(data)


@api_view(['GET'])
def get_about_broker(request):
    about = AboutBroker.objects.order_by("-id")[:3]
    data = AboutBrokerSerializer(about, many=True).data
    return Response(data)


@api_view(['GET'])
def get_broker(request):
    broker = Broker.objects.order_by("-id")[:8]
    data = BrokerSerializer(broker, many=True).data
    return Response(data)


@api_view(['GET'])
def get_step(request):
    step = Step.objects.order_by("-id")[:3]
    data = StepSerializer(step, many=True).data
    return Response(data)


@api_view(['GET'])
def get_option(request):
    option = PaymentOption.objects.order_by("-id")[:3]
    data = PaymentOptionSerializer(option, many=True).data
    return Response(data)


@api_view(['GET'])
def get_bid(request):
    bid = Bid.objects.all()
    data = BidSerializer(bid, many=True).data
    return Response(data)


@api_view(['POST'])
def set_bid(request):
    Bid.objects.create(
        name=request.POST.get('name'),
        phone_number=request.POST.get('phone_number'),
        email=request.POST.get('email'),
    )

    context = {
        'success': True,
        'message': 'created'
    }
    return Response(context)
