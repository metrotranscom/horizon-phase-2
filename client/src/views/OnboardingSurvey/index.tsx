import React from 'react'
import { Link } from 'react-router-dom'
import { Helmet } from 'react-helmet'
import { ChildDataProps, withApollo, graphql, compose, QueryOpts } from 'react-apollo'
import { RouteComponentProps } from 'react-router'
import gql from 'graphql-tag'
import {
  Button,
  Container,
  Grid,
  Header,
  Icon,
  Image,
  Label,
  Menu,
  Message,
  Responsive,
  Segment,
  Sidebar,
  Transition,
} from 'semantic-ui-react'
import { Form, Input } from 'formsy-semantic-ui-react'
import { stepQuery } from 'src/Queries'
import { StepQueryParams, Step, StepQueryResponse, StepRouteParams } from 'src/Types'
import { constructInnerHTML } from 'src/Helpers'
import cookie from 'react-cookies'
import CustomHeader from 'src/components/CustomHeader/'
import Main from 'src/components/Main/'
import { MOB, translate } from 'src/Translate'
import './style.css'

const queryString = require('query-string')

type State = {
  isSubmitting: boolean
  zipcode: string
  errorMsg: string
  contentBoxVisible: boolean
}

const surveyMutation = gql`
  mutation createSurveyResponse($zipcode: String!, $sessionId: UUID!) {
    createSurveyResponse(zipcode: $zipcode, sessionId: $sessionId) {
      error
    }
  }
`
type SurveyMutationResponse = {
  error: string
}

type SurveyMutationParams = {
  zipcode: string
  sessionId: string
}

type OwnProps = RouteComponentProps<StepRouteParams>
type StepQueryProps = ChildDataProps<StepQueryParams, StepQueryResponse> & {
  surveyMutation: Function
}
type Props = StepQueryProps & OwnProps

class OnboardingSurveyView extends React.Component<Props, State> {
  state = {
    isSubmitting: false,
    zipcode: '',
    errorMsg: '',
    contentBoxVisible: false,
  }

  componentDidMount = () => {
    setTimeout(() => {
      this.setState({ contentBoxVisible: true })
    }, 1000)
  }

  onValidSubmit = async () => {
    this.setState({ errorMsg: '', isSubmitting: true })
    const { zipcode } = this.state

    let { data } = await this.props.surveyMutation({
      variables: { zipcode, sessionId: cookie.load('session_id') },
    })
    this.setState({ isSubmitting: false })

    if (!data.createSurveyResponse.error) {
      this.props.history.push(
        `/onboarding/choose-category/10006?lang=${
          queryString.parse(this.props.location.search).lang
        }`
      )
    } else {
      console.error('Error')
    }
  }

  onFieldChange = (e: React.FormEvent<HTMLInputElement>) => {
    const { name, value, checked, type } = e.currentTarget
    const newVal = type === 'checkbox' ? checked : value
    this.setState(prevState => ({
      ...prevState,
      [name]: newVal,
    }))
  }

  render() {
    const { step, loading } = this.props.data
    const { contentBoxVisible, zipcode, isSubmitting, errorMsg } = this.state

    return (
      <div className="view" id="onboarding-survey-view">
        <Main stepId={this.props.match.params.stepId}>
          <Form
            className="forma"
            loading={loading || isSubmitting}
            onValidSubmit={this.onValidSubmit}
          >
            <CustomHeader
              stepId={this.props.match.params.stepId}
              lang={queryString.parse(this.props.location.search).lang}
            />
            <Transition visible={contentBoxVisible} animation="fade" duration={500}>
              <div className="content-box">
                <h1 className="">{step && step.publicField1}</h1>
                <br />
                <p
                  className="large"
                  dangerouslySetInnerHTML={constructInnerHTML(step && step.publicField2)}
                />
                <Form.Input
                  name="zipcode"
                  label={step && step.publicField3}
                  value={zipcode}
                  placeholder=""
                  onChange={this.onFieldChange}
                />
                <div className="btn-holder">
                  <Button className="btn primary" disabled={isSubmitting}>
                    {step && step.publicField6}
                  </Button>
                </div>
              </div>
            </Transition>
          </Form>
        </Main>
      </div>
    )
  }
}

export default compose(
  graphql(surveyMutation, { name: 'surveyMutation' }),
  graphql<Props, StepQueryResponse>(stepQuery, {
    options: (props: OwnProps): QueryOpts<StepQueryParams> => ({
      variables: {
        id: parseInt(props.match.params.stepId),
        lang: queryString.parse(props.location.search).lang
          ? queryString.parse(props.location.search).lang
          : 'en',
        renderMdToHtml: true,
      },
    }),
  })
)(OnboardingSurveyView)
