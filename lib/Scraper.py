from bs4 import BeautifulSoup
import requests
from Course import Course


class Scraper:
    def __init__(self):
        self.url = "http://learn-co-curriculum.github.io/site-for-scraping/courses"
        self.page = None
        self.courses = []

    def get_page(self):
        """Fetch the HTML page and return BeautifulSoup object"""
        response = requests.get(self.url)
        self.page = BeautifulSoup(response.text, 'html.parser')
        return self.page

    def get_courses(self):
        """Parse course elements from the page"""
        if self.page is None:
            self.get_page()
        
        # Find all course offerings based on the HTML structure
        course_offerings = self.page.select('.post')
        return course_offerings

    def make_courses(self):
        """Create Course objects from parsed data"""
        if self.page is None:
            self.get_page()
        
        course_offerings = self.get_courses()
        self.courses = []

        for offering in course_offerings:
            title = offering.select("h2")[0].text if offering.select("h2") else ''
            schedule = offering.select(".date")[0].text if offering.select(".date") else ''
            description = offering.select("p")[0].text if offering.select("p") else ''
            
            course = Course(title=title, schedule=schedule, description=description)
            self.courses.append(course)

        return self.courses
