<!DOCTYPE html>
<HTML lang="en">

<HEAD>
    <TITLE>AirBnb Clone</TITLE>
    <LINK rel="stylesheet" href="static/styles/4-common.css">
    <LINK rel="stylesheet" href="static/styles/3-header.css">
    <LINK rel="stylesheet" href="static/styles/3-footer.css">
    <LINK rel="stylesheet" href="static/styles/6-filters.css">
    <LINK rel="stylesheet" href="static/styles/8-places.css">
    <LINK rel="icon" href="static/images/icon.png" type="image/png">
</HEAD>

<BODY>
    <HEADER>
        <DIV class="logo"></DIV>
    </HEADER>
    <DIV class="container">
        <SECTION class="filters">
            <BUTTON type="button">Search</BUTTON>
            <DIV class="locations">
                <H3>States</H3>
                <H4>&nbsp;</H4>
                    <UL class="popover">
                    {% for state in states.values() | sort(attribute="name") %}
                        <LI><H2>{{ state.name }}</H2></LI>
                        <LI>
                            <UL class="popover_l">
                            {% for city in state.cities | sort(attribute="name") %}
                            <LI>{{ city.name }}</LI>
                            {% endfor %}
                            </UL>
                        </LI>
                    {% endfor %}
                  </UL>
            </DIV>
            <DIV class="amenities">
                <H3>Amenities</H3>
                <H4>&nbsp;</H4>
                <UL class="popover">
                {% for amenity in amenities.values() | sort(attribute="name") %}
                <LI>{{ amenity.name }}</LI>
                {% endfor %}
                </UL>
            </DIV>
        </SECTION>
        <SECTION class="places">
            <DIV class="places_title">
                <h1>Places</h1>
            </DIV>
            <DIV class="articles">
                {% for place in places.values() | sort(attribute="name") %}
                <ARTICLE>
                    <DIV class="price_title">
                        <DIV class="article_title">
                            <H2>{{ place.name }}</H2>
                        </DIV>
                        <DIV class="price_by_night">
                            <DIV class="price">
                                &#36;{{ place.price_by_night }}
                            </DIV>
                        </DIV>
                    </DIV>
                    <DIV class="information">
                        <DIV class="max_guest">
                            <DIV class="guest_icon">
                            </DIV>
                            <DIV class="guest_number">
                                <H2>{{ place.max_guest }} Guests</H2>
                            </DIV>
                        </DIV>
                        <DIV class="number_rooms">
                            <DIV class="rooms_icon">
                            </DIV>
                            <DIV class="rooms_number">
                                <H2>{{ place.number_rooms }} Rooms</H2>
                            </DIV>
                        </DIV>
                        <DIV class="number_bathrooms">
                            <DIV class="bathrooms_icon">
                            </DIV>
                            <DIV class="bathrooms_number">
                                <H2>{{ place.number_bathrooms }} Bathrooms</H2>
                            </DIV>
                        </DIV>
                    </DIV>
                    <DIV class="user">
                        <b>Owner:</b> {{ place.user.first_name }} {{ place.user.last_name }}
                    </DIV>
                    <DIV class="description">
                        {{ place.description | safe }}
                    </DIV>
                </ARTICLE>
            {% endfor %}
        </DIV>
        </SECTION>
    </DIV>
    <FOOTER>
        Holberton School
    </FOOTER>
</BODY>

</HTML>

