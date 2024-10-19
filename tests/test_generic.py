"""Test the generic pipeline."""

from rago import Rago
from rago.augmented.generic import GenericAugmented
from rago.generation.generic import GenericGeneration
from rago.retrieval.generic import GenericRetrieval, SourceContentBase


def test_generic_string() -> None:
    documents = [
        (
            'Blue Whale: The Blue Whale is the largest animal ever known to have existed, even bigger than the largest dinosaurs. Found in oceans worldwide, these marine mammals can reach lengths of up to 30 meters and weigh as much as 200 tons. Their heart alone can be the size of a small car. Despite their massive size, Blue Whales feed primarily on tiny shrimp-like animals called krill, consuming up to 4 tons of it each day during feeding season. They are known for their loud vocalizations, which can be heard over vast distances underwater and are believed to play a role in communication and navigation. Blue Whales were once abundant but were brought to near extinction by whaling; they are currently classified as endangered.'  # noqa
        ),
        (
            'Peregrine Falcon: The Peregrine Falcon is renowned as the fastest animal on the planet, capable of reaching speeds over 240 miles per hour during its characteristic hunting stoop (high-speed dive). Found on every continent except Antarctica, these raptors have a blue-gray back, barred white underparts, and a distinctive black head. They prey mainly on other birds, catching them in mid-air with incredible agility and precision. Peregrine Falcons have made remarkable recoveries in population after being endangered due to pesticide use, particularly DDT, which caused thinning of their eggshells. Conservation efforts have included captive breeding and reintroduction programs, making them a success story in wildlife management.'  # noqa
        ),
        (
            'Giant Panda: The Giant Panda is a bear species endemic to China, easily recognized by its distinctive black-and-white coat and rotund body. Pandas inhabit mountainous regions with dense bamboo forests, which make up more than 99% of their diet. An adult panda can consume between 26 to 84 pounds of bamboo daily to meet its energy needs. They have a pseudo-thumb, an extended wrist bone that helps them grasp bamboo stems. Giant Pandas are solitary animals with a slow reproductive rate, factors that have contributed to their vulnerability. Extensive conservation efforts, including habitat preservation and captive breeding, have improved their status from endangered to vulnerable.'  # noqa
        ),
        (
            'Cheetah: The Cheetah is the world\'s fastest land animal, capable of sprinting at speeds up to 70 miles per hour in short bursts covering distances up to 500 meters. Native to Africa and central Iran, cheetahs have slender bodies, deep chests, spotted coats, and distinctive black "tear marks" running from the corners of their eyes down to their mouths. These adaptations help reduce glare and aid in hunting prey during daylight hours. Unlike other big cats, cheetahs cannot roar but purr loudly when content. They face threats from habitat loss, human-wildlife conflict, and reduced genetic diversity, leading to conservation programs focused on habitat preservation and reducing human encroachment.'  # noqa
        ),
        (
            'Komodo Dragon: The Komodo Dragon is the largest living species of lizard, found on several Indonesian islands, including its namesake, Komodo. Growing up to 3 meters in length and weighing around 70 kilograms, these formidable predators have rugged, armored scales and powerful limbs. They are carnivorous, feeding on large prey such as deer, pigs, and even water buffalo, using a combination of sharp teeth and toxic saliva containing anticoagulant properties. Komodo Dragons have an acute sense of smell, detecting carrion from several kilometers away using their forked tongues. Due to their limited range and declining population, they are classified as endangered, with conservation efforts focused on habitat protection and reducing human interference.'  # noqa
        ),
        (
            "Arctic Fox: The Arctic Fox is a small mammal adapted to living in the harsh conditions of the Arctic tundra. It has a thick, insulating coat that changes color with the seasons—white in the winter to blend with snow and brown or gray in the summer to match the tundra's rocks and plants. Weighing between 3 to 8 kilograms, Arctic Foxes have a compact body shape, short muzzle, and furry soles to minimize heat loss. They are opportunistic feeders, preying on lemmings, voles, birds, and fish, and scavenging on carcasses left by polar bears. Their keen hearing helps them locate prey under snow. Climate change and competition from Red Foxes encroaching northward pose significant threats to their survival."  # noqa
        ),
        (
            'Monarch Butterfly: The Monarch Butterfly is a migratory species famous for its long-distance seasonal journeys across North America. Recognizable by their striking orange and black wing patterns, Monarchs undertake an annual migration of up to 3,000 miles from Canada and the United States to overwintering sites in central Mexico and coastal California. This migration spans multiple generations, with butterflies laying eggs along the route. The caterpillars feed exclusively on milkweed plants, which contain toxins that make them unpalatable to predators. Threats to Monarch populations include habitat loss, climate change, and pesticide use, prompting conservation efforts to preserve migratory corridors and host plants.'  # noqa
        ),
        (
            "Great White Shark: The Great White Shark is one of the ocean's most formidable predators, known for its size, speed, and sharp senses. Found in coastal surface waters of all major oceans, they can grow up to 6 meters in length and weigh over 2,000 kilograms. Great Whites have a torpedo-shaped body, enabling them to swim at speeds up to 25 miles per hour. They possess highly developed sensory organs, including the ability to detect electromagnetic fields produced by other animals. Their diet consists mainly of marine mammals like seals and sea lions, as well as fish and seabirds. While often feared, Great White Sharks play a crucial role in marine ecosystems by maintaining the balance of species below them in the food chain."  # noqa
        ),
        (
            'Honey Bee: The Honey Bee is a social flying insect notable for its role in pollination and for producing honey and beeswax. Living in well-organized colonies consisting of a single queen, numerous female worker bees, and male drones, they exhibit complex behaviors and communication methods, such as the ¸"waggle dance" to inform others about the location of food sources. Honey Bees are vital to agriculture, pollinating a wide variety of crops. They collect nectar and pollen from flowers, converting the nectar into honey stored within the hive as a food source for the colony. Threats like colony collapse disorder, pesticides, habitat loss, and diseases have significantly impacted bee populations, leading to global concerns over pollination services.'  # noqa
        ),
        (
            'Emperor Penguin: The Emperor Penguin is the tallest and heaviest of all living penguin species, endemic to Antarctica. Standing up to 1.2 meters tall and weighing between 22 to 45 kilograms, they are well adapted to the extreme cold with a dense plumage and a layer of subdermal fat. Emperor Penguins are unique for their breeding cycle during the Antarctic winter, where males incubate a single egg for about 65 days while fasting, huddling together for warmth in temperatures that can drop below -50°C. They feed on fish, krill, and squid, diving to depths over 500 meters. Climate change poses a significant threat to their sea ice habitat, affecting breeding and feeding grounds.'  # noqa
        ),
    ]
    retrieval = GenericRetrieval()
    augmented = GenericAugmented()
    generation = GenericGeneration()

    rag = Rago(
        augmented=augmented,
        retrieval=retrieval,
        generation=generation,
    )

    query = 'Is there any animals larger than a dinosaur?'
    result = rag.prompt(query)
